/* Better Vibe landing — scroll story, mascot guide, download gate. No dependencies. */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  var reduce = root.classList.contains("rm");
  var clamp = function (v, a, b) { return v < a ? a : v > b ? b : v; };
  var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
  var store = {
    get: function (s, k) { try { return window[s].getItem(k); } catch (e) { return null; } },
    set: function (s, k, v) { try { window[s].setItem(k, v); } catch (e) { /* storage blocked: stay stateless */ } }
  };
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };
  var hasIO = "IntersectionObserver" in window;
  var footIn = false;

  /* ---------- reveal on view ---------- */
  var revealEls = $$("[data-reveal], .wordmark, .ch-end");
  if (hasIO && !reduce) {
    var rio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); rio.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -12% 0px" });
    revealEls.forEach(function (el) { rio.observe(el); });
  } else revealEls.forEach(function (el) { el.classList.add("in"); });

  /* ---------- hero: live dictation → clean prompt loop ---------- */
  var stage = $(".stage-ui");
  if (stage) {
    var words = $$(".pill-text span", stage), timer = null, heroVisible = true;
    var showAll = function () { words.forEach(function (w) { w.classList.add("on"); }); stage.classList.add("done"); };
    var run = function () {
      clearTimeout(timer);
      stage.classList.remove("done");
      words.forEach(function (w) { w.classList.remove("on", "fresh"); });
      var i = 0;
      var step = function () {
        if (!heroVisible) { timer = setTimeout(step, 400); return; }
        if (i < words.length) {
          words[i].classList.add("on", "fresh");
          if (i >= 4) words[i - 4].classList.remove("fresh");
          i++;
          timer = setTimeout(step, 150 + Math.random() * 110);
        } else {
          timer = setTimeout(function () {
            stage.classList.add("done");
            timer = setTimeout(run, 4200);
          }, 700);
        }
      };
      timer = setTimeout(step, 900);
    };
    if (reduce) showAll(); else run();
    if (hasIO) new IntersectionObserver(function (es) { heroVisible = es[0].isIntersecting; }).observe(stage);

    var icon = $(".stage-icon"), hero = $(".hero");
    if (icon && !reduce && matchMedia("(hover:hover) and (pointer:fine)").matches) {
      hero.addEventListener("pointermove", function (ev) {
        var r = hero.getBoundingClientRect();
        var x = (ev.clientX - r.left) / r.width - .5, y = (ev.clientY - r.top) / r.height - .5;
        icon.style.setProperty("--ry", (-10 + x * 16).toFixed(2) + "deg");
        icon.style.setProperty("--rx", (6 - y * 12).toFixed(2) + "deg");
      });
      hero.addEventListener("pointerleave", function () { icon.style.removeProperty("--ry"); icon.style.removeProperty("--rx"); });
    }
  }

  /* ---------- typed lanes (speed) ---------- */
  var lanes = $$(".lane-text").map(function (p) {
    var full = p.textContent;
    p.innerHTML = "";
    var typed = doc.createElement("span"), rest = doc.createElement("span");
    typed.className = "typed"; rest.className = "rest";
    p.appendChild(typed); p.appendChild(rest);
    return { typed: typed, rest: rest, full: full, last: -1 };
  });
  var setLane = function (l, f) {
    var n = Math.round(clamp(f, 0, 1) * l.full.length);
    if (n === l.last) return;
    l.last = n; l.typed.textContent = l.full.slice(0, n); l.rest.textContent = l.full.slice(n);
  };

  /* ---------- cleanup lab ---------- */
  var labWords = $$(".lab-said .w.x").sort(function (a, b) { return a.dataset.n - b.dataset.n; });
  var labTags = $$(".lab-why li"), tokEl = $(".tok-in"), clean = $(".ch-clean");
  var tokFrom = tokEl ? +tokEl.dataset.from : 0, tokTo = tokEl ? +tokEl.dataset.to : 0;

  var handlers = {
    speed: function (el, p) {
      var v = clamp(p / .62, 0, 1);
      setLane(lanes[1], v); setLane(lanes[0], v / 3);
      el.style.setProperty("--x3", v >= 1 ? 1 : 0);
    },
    clean: function (el, p) {
      var s = clamp((p - .08) / .62, 0, 1), n = Math.round(s * labWords.length), seen = {};
      labWords.forEach(function (w, i) {
        var on = i < n; w.classList.toggle("on", on);
        if (on) seen[w.dataset.k] = 1;
      });
      labTags.forEach(function (t) { t.classList.toggle("on", !!seen[t.dataset.k]); });
      if (tokEl) tokEl.textContent = Math.round(tokFrom - (tokFrom - tokTo) * s);
      el.style.setProperty("--sent", clamp((p - .66) / .16, 0, 1).toFixed(3));
      el.style.setProperty("--done", s >= 1 ? 1 : 0);
    },
    tour: function (el, p) { el.style.setProperty("--p", ease(p).toFixed(4)); },
    levels: function (el, p) {
      var track = $(".tiers", el);
      var shift = Math.max(0, track.scrollWidth - window.innerWidth);
      el.style.setProperty("--shift", shift + "px");
      el.style.setProperty("--p", clamp((p - .1) / .8, 0, 1).toFixed(4));
    }
  };

  /* ---------- scroll engine ---------- */
  var scrubs = $$("[data-scrub]");
  var ANCHORS = { speed: ".race", clean: ".lab", levels: ".tiers" };
  var progressBar = $(".progress span"), header = $(".top");
  var ticking = false;

  var fits = function () {
    // A pinned chapter whose content is taller than the screen (small phones,
    // big text) would be clipped: let it scroll normally instead.
    $$(".pin").forEach(function (sec) {
      var st = $(".sticky", sec);
      sec.classList.remove("no-pin");
      if (reduce || st.scrollHeight > window.innerHeight + 2) sec.classList.add("no-pin");
    });
    var lv = $(".ch-levels");
    if (lv && window.innerWidth < 640) lv.classList.add("no-pin");
  };

  var update = function () {
    ticking = false;
    var vh = window.innerHeight, sc = window.scrollY || root.scrollTop;
    var max = root.scrollHeight - vh;
    if (progressBar) progressBar.style.transform = "scaleX(" + (max > 0 ? sc / max : 0).toFixed(4) + ")";
    if (header) header.classList.toggle("solid", sc > 12);
    scrubs.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -vh || r.top > vh * 2) return;
      var p;
      if (reduce) p = 1;
      else if (el.dataset.mode === "view") p = clamp((vh - r.top) / (vh * .85), 0, 1);
      else if (el.classList.contains("no-pin")) {
        // Unpinned on small screens: drive the animation by the key visual itself.
        var a = el.querySelector(ANCHORS[el.dataset.scrub] || ".sticky").getBoundingClientRect();
        p = clamp((vh * .92 - a.top) / (Math.min(a.height, vh * .6) + vh * .25), 0, 1);
      }
      else p = clamp(-r.top / Math.max(1, r.height - vh), 0, 1);
      var h = handlers[el.dataset.scrub]; if (h) h(el, p);
    });
  };
  var onScroll = function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  fits(); update();
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", function () { fits(); onScroll(); });
  window.addEventListener("load", function () { fits(); update(); });

  /* ---------- big number count-up ---------- */
  var num = $(".num[data-count]");
  if (num && hasIO && !reduce) {
    var target = +num.dataset.count; num.textContent = "−0";
    var nio = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return;
      nio.disconnect();
      var t0 = performance.now();
      (function tick(t) {
        var k = clamp((t - t0) / 1400, 0, 1);
        num.textContent = "−" + Math.round(ease(k) * target);
        if (k < 1) requestAnimationFrame(tick);
      })(t0);
    }, { threshold: .6 });
    nio.observe(num);
  }

  /* ---------- how it works: active step ---------- */
  var steps = $$(".step"), views = $$(".how-view");
  var setStep = function (i) {
    steps.forEach(function (s, k) { s.classList.toggle("on", k === i); });
    views.forEach(function (v, k) {
      var on = k === i; v.classList.toggle("on", on);
      var vid = $("video", v); if (vid) { if (on) playVid(vid); else vid.pause(); }
    });
  };
  if (steps.length) {
    setStep(0);
    if (hasIO) {
      var sio = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) setStep(steps.indexOf(e.target)); });
      }, { rootMargin: "-48% 0px -48% 0px" });
      steps.forEach(function (s) { sio.observe(s); });
    }
  }

  /* ---------- videos: play only when visible, never for reduced motion / data saver ---------- */
  var saveData = !!(navigator.connection && navigator.connection.saveData);
  var autoOK = !reduce && !saveData;
  function playVid(v) {
    if (!autoOK) return;
    if (v.preload === "none") v.preload = "auto";
    var pr = v.play(); if (pr && pr.catch) pr.catch(function () { v.controls = true; });
  }
  var vids = $$("video[data-auto]");
  if (!autoOK) vids.forEach(function (v) { v.controls = true; v.removeAttribute("loop"); });
  else if (hasIO) {
    var vio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target, inStage = v.closest(".how-view");
        if (e.isIntersecting && (!inStage || inStage.classList.contains("on"))) playVid(v); else v.pause();
      });
    }, { threshold: .35 });
    vids.forEach(function (v) { vio.observe(v); });
  }
  vids.forEach(function (v) {
    v.addEventListener("error", function () { v.controls = false; }, true);
  });

  var gate = $(".gate");
  /* ---------- mascot guide ---------- */
  var guide = $(".guide");
  if (guide) {
    var lines = {}; try { lines = JSON.parse(guide.dataset.lines); } catch (e) { /* keep static line */ }
    var base = guide.dataset.base, img = $(".guide-img", guide), say = $(".guide-say", guide);
    var bubble = $(".guide-bubble", guide), xBtn = $(".guide-x", guide);
    var cur = "hero", small = window.matchMedia("(max-width: 40rem)"), quietT = null, typeT = null;
    ["happy", "encourage", "celebrate", "streak"].forEach(function (p) { var i = new Image(); i.src = base + "mascot-" + p + ".webp"; });

    // The full line sits invisible underneath so the bubble keeps its final size
    // while the visible copy types out: no layout shift, nothing clipped.
    var typeOut = function (text) {
      clearTimeout(typeT);
      say.innerHTML = "";
      var full = doc.createElement("span"), typed = doc.createElement("span");
      full.className = "full"; typed.className = "typed"; typed.setAttribute("aria-hidden", "true");
      full.textContent = text; say.appendChild(full); say.appendChild(typed);
      if (reduce) { typed.textContent = text; return; }
      var i = 0;
      (function go() { i += 2; typed.textContent = text.slice(0, i); if (i < text.length) typeT = setTimeout(go, 16); })();
    };
    var quiet = function () {
      clearTimeout(quietT);
      guide.classList.remove("quiet");
      quietT = setTimeout(function () { guide.classList.add("quiet"); }, small.matches ? 5000 : 6500);
    };
    var setLine = function (key) {
      if (!lines[key] || key === cur) return;
      cur = key;
      var pose = lines[key][0], text = lines[key][1];
      bubble.classList.add("swap");
      setTimeout(function () {
        img.src = base + "mascot-" + pose + ".webp";
        img.classList.remove("hop"); void img.offsetWidth; if (!reduce) img.classList.add("hop");
        bubble.classList.remove("swap");
        typeOut(text);
        quiet();
      }, reduce ? 0 : 180);
    };
    if (small.matches) {
      // Phones: the greeting would sit on top of the hero buttons. Say hi on the first scroll instead.
      guide.classList.add("quiet");
      window.addEventListener("scroll", function first() { window.removeEventListener("scroll", first); quiet(); }, { passive: true });
    } else quiet();
    img.addEventListener("click", function () { if (!guide.classList.contains("min")) { if (guide.classList.contains("quiet")) quiet(); else guide.classList.add("quiet"); } });
    if (hasIO) {
      var gio = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) setLine(e.target.dataset.guide); });
      }, { rootMargin: "-45% 0px -45% 0px" });
      $$("[data-guide]").forEach(function (s) { gio.observe(s); });
      var foot = $(".foot");
      if (foot) new IntersectionObserver(function (es) { footIn = es[0].isIntersecting; guide.classList.toggle("away", footIn || (gate && gate.open)); }, { rootMargin: "0px 0px -20% 0px" }).observe(foot);
    }
    var setMin = function (m) {
      guide.classList.toggle("min", m);
      xBtn.setAttribute("aria-label", m ? xBtn.dataset.show : xBtn.dataset.hide);
      img.setAttribute("role", m ? "button" : "presentation");
      if (m) { img.tabIndex = 0; img.setAttribute("aria-label", xBtn.dataset.show); } else { img.removeAttribute("tabindex"); img.removeAttribute("aria-label"); }
      store.set("localStorage", "bv-guide-min", m ? "1" : "0");
    };
    xBtn.addEventListener("click", function () { setMin(true); img.focus(); });
    var reopen = function () { if (guide.classList.contains("min")) { setMin(false); quiet(); xBtn.focus(); } };
    img.addEventListener("click", reopen);
    img.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); reopen(); } });
    if (store.get("localStorage", "bv-guide-min") === "1") setMin(true);
    bubble.addEventListener("click", function () { guide.classList.add("quiet"); });
  }

  /* ---------- download gate ---------- */
  if (gate && typeof gate.showModal === "function") {
    var cfg = {}; try { cfg = JSON.parse(gate.dataset.cfg); } catch (e) { /* defaults */ }
    var opener = null;
    var show = function (name) {
      $$(".gate-step", gate).forEach(function (s) { s.hidden = s.dataset.step !== name; });
      var step = $('.gate-step[data-step="' + name + '"]', gate);
      var target = name === "ask" ? $("[data-follow]", step) : $("h2", step);
      if (target) target.focus();
    };
    var next = function () { show(cfg.dl ? "go" : "soon"); store.set("sessionStorage", "bv-gate", "1"); };
    var open = function (ev) {
      // Already passed the gate this visit and a real download exists: go straight there.
      if (cfg.dl && store.get("sessionStorage", "bv-gate") === "1") return;
      ev.preventDefault();
      opener = ev.currentTarget;
      gate.classList.remove("followed");
      if (guide) guide.classList.add("away");
      gate.showModal();
      show(store.get("sessionStorage", "bv-gate") === "1" ? (cfg.dl ? "go" : "soon") : "ask");
    };
    $$("[data-download]").forEach(function (a) {
      if (cfg.dl) a.href = cfg.dl;
      a.addEventListener("click", open);
    });
    $("[data-follow]", gate).addEventListener("click", function () {
      gate.classList.add("followed");
      setTimeout(next, 250); // let the new tab open first
    });
    $("[data-skip]", gate).addEventListener("click", next);
    $$("[data-close]", gate).forEach(function (b) { b.addEventListener("click", function () { gate.close(); }); });
    gate.addEventListener("click", function (e) {
      if (e.target !== gate) return;
      var r = gate.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) gate.close(); // backdrop
    });
    gate.addEventListener("close", function () {
      if (guide && !footIn) guide.classList.remove("away");
      if (opener && opener.focus) opener.focus();
    });
  }

  /* ---------- FR suggestion on the English page ---------- */
  var banner = $(".lang-banner");
  if (banner) {
    var lang = (navigator.languages && navigator.languages[0]) || navigator.language || "";
    if (/^fr\b/i.test(lang) && store.get("localStorage", "bv-lang-banner") !== "0") banner.hidden = false;
    $(".lang-banner-x", banner).addEventListener("click", function () { banner.hidden = true; store.set("localStorage", "bv-lang-banner", "0"); });
  }
})();
