"""Landing page (index.html) for EN (root) and FR (/fr/). Imported by build.py.

Single source of truth for the download target: DOWNLOAD_URL. Leave it empty
while the app is not publicly downloadable; the download gate then says
"coming soon" instead of sending people to a dead link.
"""
import html, json
from urllib.parse import quote

BASE = "https://connected-mate.github.io/better-vibe-site/"
DOWNLOAD_URL = ""  # e.g. "https://apps.apple.com/app/id6819835715" once live
LINKEDIN = "https://www.linkedin.com/in/alex-cormeraie/"
MAIL = "alex.connectedmate@gmail.com"
SPEECH_STUDY = "https://arxiv.org/abs/1608.07323"

# Lab example captured from the real app (Labo / Lab screen, 2026-10-28).
# word|f = filler, word|c = self-correction, word|r = repetition.
LAB = {
 "fr": {
  "said": "alors|f euh|f du|f coup|f J'ai un bug dans LoginView.swift quand je clique sur le bouton. connexion|c Ça plante enfin|c non|c ça|r plante|r pas, ça reste bloqué sur le spinner. et|f euh|f voilà|f Est-ce que tu peux regarder pourquoi Merci.",
  "sent": "J'ai un bug dans LoginView.swift quand je clique sur le bouton. Ça plante pas, ça reste bloqué sur le spinner. Est-ce que tu peux regarder pourquoi<mark>&nbsp;?</mark> Merci.",
  "tok_in": 71, "tok_out": 54, "secs": "1,2",
 },
 "en": {
  "said": "so|f uh|f There's a bug in LoginView.swift when I click the sign|c in|c button. It crashes,|c well|f no|c it|c doesn't crash; it just stays stuck on the spinner forever. and|f uh|f yeah|f Can you look at why? Thanks.",
  "sent": "There's a bug in LoginView.swift when I click the <mark>sign-in</mark> button. It doesn't crash; it just stays stuck on the spinner forever. Can you look at why? Thanks.",
  "tok_in": 48, "tok_out": 41, "secs": "1.6",
 },
}

T = {
"fr": {
 "lang": "fr", "locale": "fr_FR", "alt_locale": "en_US",
 "title": "Better Vibe — Parle. Ton prompt est prêt. App Mac gratuite",
 "desc": "Better Vibe transforme ta voix en prompts propres pour tes agents IA de code. Parle 3× plus vite que tu ne tapes, envoie moins de tokens. Gratuit, 100 % sur ton Mac.",
 "skip": "Aller au contenu",
 "nav": [("#produit", "La vraie app"), ("#comment", "Comment ça marche"), ("#prive", "Confidentialité")],
 "lang_switch": "EN", "lang_switch_label": "English version",
 "dl": "Télécharger", "dl_long": "Télécharger, c'est gratuit",
 "soon": "Bientôt sur le Mac App Store",
 "hero_eyebrow": "App Mac gratuite, pour les vibe coders",
 "h1": ["Parle.", "Ton prompt", "est prêt."],
 "lede": "Tu dictes ton idée avec tes « euh » et tes « non, attends ». Better Vibe la nettoie et en fait un prompt clair pour ton agent IA. Plus vite qu'au clavier, et avec moins de tokens.",
 "see_demo": "Voir la vraie app",
 "hero_meta": ["macOS 13 ou plus", "Mac Apple Silicon", "100 % sur ton Mac"],
 "pill_listen": "Écoute",
 "pill_words": "alors je voudrais qu'on reprenne la page d'accueil de l'application parce que aujourd'hui quand on arrive dessus on comprend pas tout de suite",
 "panel_title": "Prompt amélioré", "panel_copied": "Copié",
 "panel_text": "Reprends la page d'accueil : à l'arrivée, on ne comprend pas tout de suite ce que fait l'app.",
 "hero_stage_label": "Animation : une phrase dictée apparaît mot à mot, puis devient un prompt propre, copié.",
 "scroll": "Scrolle",
 # chapters
 "c1_k": "01 · La vitesse",
 "c1_h": "Ta voix va trois fois plus vite que tes doigts.",
 "c1_p": "Parler est environ trois fois plus rapide que taper. Pendant que tu cherches la bonne touche, ton idée est déjà dite.",
 "c1_kb": "Au clavier", "c1_voice": "À la voix",
 "c1_line": "Ajoute un mode sombre à la page des réglages et garde le choix après un redémarrage.",
 "c1_src": "Source : Ruan et al., Stanford, 2016",
 "c2_k": "02 · Le nettoyage",
 "c2_h": "Tu parles comme tu penses. Better Vibe écrit comme un pro.",
 "c2_said": "Ce que tu as dit", "c2_sent": "Ce qui part à l'agent",
 "c2_tok_said": "tokens dits", "c2_tok_sent": "tokens envoyés",
 "c2_why": "Pourquoi ces mots ont changé",
 "tags": {"f": "Mot de remplissage", "c": "Tu t'es repris", "r": "Répétition"},
 "c2_note": "Exemple réel, tiré du Labo de l'app.",
 "c3_k": "03 · Les tokens",
 "c3_unit": "de tokens", "c3_sub": "sur cette seule phrase.",
 "c3_p": "Ton agent lit chaque mot que tu lui envoies, et chaque mot se paie : en tokens, en contexte, en attention. Un prompt sans bla-bla, c'est une réponse plus nette et plus de place pour ton code.",
 "c3_facts": ["{i} → {o} tokens", "{n} mots parasites retirés", "réécrit en {s} s"],
 "c4_k": "04 · La vraie app",
 "c4_h": "Pas une maquette. La vraie app, en vrai.",
 "c4_tour": "app-tour-fr-light", "c4_tour_label": "Visite de l'app Better Vibe : accueil, dictée, comment ça marche, labo.",
 "clips": [
  ("live-text-fr-light", 524, 198, "Tes mots s'affichent pendant que tu parles."),
  ("reveal-clean-fr", 520, 300, "Ton prompt est prêt, et déjà copié."),
  ("onboarding-fr-light", 822, 620, "Prêt en une minute, guidé pas à pas."),
 ],
 "c5_k": "05 · Comment ça marche",
 "c5_h": "Quatre étapes. C'est tout.",
 "steps": [
  ("Appuie sur le raccourci", "Depuis n'importe quelle app. Rappuie pour arrêter."),
  ("Dis ce que tu veux", "Comme tu l'expliquerais à un collègue."),
  ("C'est nettoyé", "Hésitations retirées, prompt structuré, sur ton Mac."),
  ("Colle-le", "⌘V dans Claude, Cursor, ChatGPT… où tu veux."),
 ],
 "panel_img": "still-menubar-panel-fr-light", "panel_alt": "Le menu de Better Vibe dans la barre des menus, avec le bouton Dicter un prompt.",
 "paste_app": "Ton agent", "paste_ph": "Demande ce que tu veux…",
 "c6_k": "06 · Privé",
 "c6_h": "Ta voix ne quitte jamais ton Mac.",
 "c6_p": "Transcription, nettoyage, prompt : tout se passe sur ta machine. Pas de compte, pas de cloud, pas de pistage.",
 "proof": [
  ("Reconnaissance vocale locale", "Whisper ou le moteur intégré d'Apple, directement sur ton Mac."),
  ("Zéro compte", "Tu ouvres, tu parles. Aucune inscription."),
  ("Aucune donnée collectée", "Écrit noir sur blanc dans notre <a href=\"privacy.html\">politique de confidentialité</a>."),
 ],
 "c7_k": "07 · Le jeu",
 "c7_h": "Chaque prompt te fait monter de niveau.",
 "c7_p": "Séries de jours, score de clarté, icônes à débloquer : ta routine devient un jeu. Bronze, argent, or… jusqu'au diamant.",
 "tiers": [("icon", "Originale"), ("tier-bronze", "Bronze"), ("tier-silver", "Argent"), ("tier-gold", "Or"), ("tier-diamond", "Diamant")],
 "end_h": "C'est gratuit. Vraiment.",
 "end_p": "Pas d'abonnement, pas de compte, pas de pub. Juste ta voix et tes prompts.",
 "end_req": "Mac Apple Silicon (M1 ou plus récent), macOS 13 Ventura ou plus récent.",
 # guide lines (mascot narration)
 "guide": {
  "hero": ("happy", "Salut ! Je te prends par la main. Scrolle, je te montre tout."),
  "c1": ("streak", "Toi, tu parles. Moi, je tape. Marché conclu ?"),
  "c2": ("encourage", "Les « euh », les « du coup », les phrases corrigées en route… je fais le ménage. Ton idée reste intacte."),
  "c3": ("happy", "Moins de mots, plus de signal. Ton agent va adorer."),
  "c4": ("happy", "Ça, c'est chez moi. Tout ce que tu vois tourne sur ton Mac."),
  "c5": ("encourage", "Quatre gestes. Au bout d'un jour, tu ne les vois même plus."),
  "c6": ("encourage", "Ce que tu dis reste entre nous. Promis."),
  "c7": ("celebrate", "Niveau supérieur ! Bon, c'est toi qui fais tout le boulot."),
  "end": ("celebrate", "Allez, on y va ? C'est gratuit."),
 },
 "guide_label": "Ton guide", "guide_hide": "Masquer le guide", "guide_show": "Afficher le guide",
 # gate
 "g1_h": "Attends, attends !",
 "g1_p": "Avant de télécharger… tu viens suivre Alex, mon créateur, sur LinkedIn ? C'est là qu'il partage les nouveautés de Better Vibe.",
 "g1_follow": "Suivre Alex sur LinkedIn", "g1_skip": "Non merci, passer au téléchargement",
 "g2_h_thanks": "Merci, ça lui fait super plaisir !",
 "g2_h": "À toi l'app !",
 "g2_p": "Better Vibe est gratuite. Bonne dictée !",
 "g2_go": "Télécharger Better Vibe",
 "g3_h": "Better Vibe arrive très bientôt",
 "g3_p": "L'app est en cours de validation sur le Mac App Store. Laisse ton e-mail ou suis Alex sur LinkedIn : tu seras prévenu dès qu'elle est en ligne.",
 "g3_mail": "Me prévenir par e-mail", "g3_mail_subject": "Préviens-moi quand Better Vibe sort",
 "g3_mail_body": "Salut Alex, préviens-moi quand Better Vibe est disponible sur le Mac App Store. Merci !",
 "g3_li": "Suivre sur LinkedIn",
 "close": "Fermer", "new_tab": "(nouvel onglet)",
 # footer
 "f_tag": "Parle. Ton prompt est prêt.",
 "f_cols": [
  ("Produit", [("#produit", "La vraie app"), ("#comment", "Comment ça marche"), ("#niveaux", "Niveaux"), ("#telecharger", "Télécharger")]),
  ("Aide", [("support.html", "Assistance"), ("privacy.html", "Confidentialité"), ("mailto:" + MAIL, "Contact")]),
 ],
 "f_li_k": "Le créateur", "f_li_h": "Suis Alex sur LinkedIn", "f_li_p": "Les nouveautés, les coulisses, et ce qui arrive ensuite.",
 "f_by": "Better Vibe par Connected Mate. Fait en France.",
 "f_top": "Revenir en haut",
 "fr_banner": "",
},
"en": {
 "lang": "en", "locale": "en_US", "alt_locale": "fr_FR",
 "title": "Better Vibe — Speak. Your prompt is ready. Free Mac app",
 "desc": "Better Vibe turns your voice into clean prompts for your AI coding agents. Speak 3× faster than you type, send fewer tokens. Free, 100% on your Mac.",
 "skip": "Skip to content",
 "nav": [("#produit", "The real app"), ("#comment", "How it works"), ("#prive", "Privacy")],
 "lang_switch": "FR", "lang_switch_label": "Version française",
 "dl": "Download", "dl_long": "Download, it's free",
 "soon": "Coming soon to the Mac App Store",
 "hero_eyebrow": "Free Mac app for vibe coders",
 "h1": ["Speak.", "Your prompt", "is ready."],
 "lede": "Say your idea out loud, “uh”s and “no, wait”s included. Better Vibe cleans it up and turns it into a clear prompt for your AI agent. Faster than typing, with fewer tokens.",
 "see_demo": "See the real app",
 "hero_meta": ["macOS 13 or later", "Apple Silicon Mac", "100% on your Mac"],
 "pill_listen": "Listening",
 "pill_words": "so I'd like us to rework the app's home page because right now when you land on it you don't get right away",
 "panel_title": "Improved prompt", "panel_copied": "Copied",
 "panel_text": "Rework the home page: when people land on it, they don't immediately understand what the app does.",
 "hero_stage_label": "Animation: a dictated sentence appears word by word, then becomes a clean prompt, copied.",
 "scroll": "Scroll",
 "c1_k": "01 · Speed",
 "c1_h": "Your voice is three times faster than your fingers.",
 "c1_p": "Speaking is about three times faster than typing. While you hunt for the right key, your idea is already out.",
 "c1_kb": "Typing", "c1_voice": "Speaking",
 "c1_line": "Add a dark mode to the settings page and keep the choice after a restart.",
 "c1_src": "Source: Ruan et al., Stanford, 2016",
 "c2_k": "02 · Cleanup",
 "c2_h": "You talk the way you think. Better Vibe writes like a pro.",
 "c2_said": "What you said", "c2_sent": "What goes to the agent",
 "c2_tok_said": "tokens said", "c2_tok_sent": "tokens sent",
 "c2_why": "Why these words changed",
 "tags": {"f": "Filler word", "c": "You corrected yourself", "r": "Repetition"},
 "c2_note": "Real example, taken from the app's Lab.",
 "c3_k": "03 · Tokens",
 "c3_unit": "tokens", "c3_sub": "on this one sentence.",
 "c3_p": "Your agent reads every word you send, and every word costs something: tokens, context, attention. A prompt without the fluff gets you a sharper answer and leaves more room for your code.",
 "c3_facts": ["{i} → {o} tokens", "{n} words cleaned up", "rewritten in {s} s"],
 "c4_k": "04 · The real app",
 "c4_h": "Not a mockup. The real app, for real.",
 "c4_tour": "app-tour-en-dark", "c4_tour_label": "Tour of the Better Vibe app: home, dictate, how it works, lab.",
 "clips": [
  ("live-text-fr-light", 524, 198, "Your words appear while you speak."),
  ("reveal-clean-fr", 520, 300, "Your prompt is ready, and already copied."),
  ("onboarding-fr-light", 822, 620, "Ready in a minute, guided step by step."),
 ],
 "c5_k": "05 · How it works",
 "c5_h": "Four steps. That's it.",
 "steps": [
  ("Press the shortcut", "From any app. Press again to stop."),
  ("Say what you want", "The way you'd explain it to a colleague."),
  ("It's cleaned up", "Hesitations removed, prompt structured, on your Mac."),
  ("Paste it", "⌘V into Claude, Cursor, ChatGPT… anywhere."),
 ],
 "panel_img": "still-menubar-panel-fr-light", "panel_alt": "The Better Vibe menu in the menu bar, with the Dictate a prompt button.",
 "paste_app": "Your agent", "paste_ph": "Ask anything…",
 "c6_k": "06 · Private",
 "c6_h": "Your voice never leaves your Mac.",
 "c6_p": "Transcription, cleanup, prompt: it all happens on your machine. No account, no cloud, no tracking.",
 "proof": [
  ("On-device speech recognition", "Whisper or Apple's built-in engine, right on your Mac."),
  ("No account", "Open it, talk. No sign-up."),
  ("No data collected", "In black and white in our <a href=\"privacy.html\">privacy policy</a>."),
 ],
 "c7_k": "07 · The game",
 "c7_h": "Every prompt levels you up.",
 "c7_p": "Day streaks, a clarity score, icons to unlock: your routine becomes a game. Bronze, silver, gold… all the way to diamond.",
 "tiers": [("icon", "Original"), ("tier-bronze", "Bronze"), ("tier-silver", "Silver"), ("tier-gold", "Gold"), ("tier-diamond", "Diamond")],
 "end_h": "It's free. Really.",
 "end_p": "No subscription, no account, no ads. Just your voice and your prompts.",
 "end_req": "Apple Silicon Mac (M1 or later), macOS 13 Ventura or later.",
 "guide": {
  "hero": ("happy", "Hi! Let me take you by the hand. Scroll, I'll show you everything."),
  "c1": ("streak", "You talk. I type. Deal?"),
  "c2": ("encourage", "The “uh”s, the “like”s, the sentences you fix halfway… I tidy them up. Your idea stays intact."),
  "c3": ("happy", "Fewer words, more signal. Your agent will love it."),
  "c4": ("happy", "This is my place. Everything you see runs on your Mac."),
  "c5": ("encourage", "Four moves. After a day, you won't even notice them."),
  "c6": ("encourage", "What you say stays between us. Promise."),
  "c7": ("celebrate", "Level up! Okay, you're doing all the work."),
  "end": ("celebrate", "Shall we? It's free."),
 },
 "guide_label": "Your guide", "guide_hide": "Hide the guide", "guide_show": "Show the guide",
 "g1_h": "Wait, wait!",
 "g1_p": "Before you download… will you follow Alex, my creator, on LinkedIn? That's where he shares what's new in Better Vibe.",
 "g1_follow": "Follow Alex on LinkedIn", "g1_skip": "No thanks, skip to download",
 "g2_h_thanks": "Thank you, that means a lot to him!",
 "g2_h": "The app is yours!",
 "g2_p": "Better Vibe is free. Happy dictating!",
 "g2_go": "Download Better Vibe",
 "g3_h": "Better Vibe is almost here",
 "g3_p": "The app is being reviewed for the Mac App Store. Leave your email or follow Alex on LinkedIn: you'll hear the moment it's live.",
 "g3_mail": "Email me when it's out", "g3_mail_subject": "Let me know when Better Vibe is out",
 "g3_mail_body": "Hi Alex, please let me know when Better Vibe is available on the Mac App Store. Thanks!",
 "g3_li": "Follow on LinkedIn",
 "close": "Close", "new_tab": "(new tab)",
 "f_tag": "Speak. Your prompt is ready.",
 "f_cols": [
  ("Product", [("#produit", "The real app"), ("#comment", "How it works"), ("#niveaux", "Levels"), ("#telecharger", "Download")]),
  ("Help", [("support.html", "Support"), ("privacy.html", "Privacy"), ("mailto:" + MAIL, "Contact")]),
 ],
 "f_li_k": "The maker", "f_li_h": "Follow Alex on LinkedIn", "f_li_p": "What's new, behind the scenes, and what's coming next.",
 "f_by": "Better Vibe by Connected Mate. Made in France.",
 "f_top": "Back to top",
 "fr_banner": "Tu parles français ? <a href=\"fr/\" hreflang=\"fr\" lang=\"fr\">Voir le site en français</a>",
},
}

def _fr_typo(v):
    """French spacing: no line break inside « » or before ? ! : ;"""
    if isinstance(v, str):
        for a, b in (("« ", "«\u00a0"), (" »", "\u00a0»"), (" ?", "\u202f?"), (" !", "\u202f!"), (" :", "\u00a0:"), (" ;", "\u202f;"), (" %", "\u00a0%")):
            v = v.replace(a, b)
        return v
    if isinstance(v, (list, tuple)):
        return type(v)(_fr_typo(x) for x in v)
    if isinstance(v, dict):
        return {k: _fr_typo(x) for k, x in v.items()}
    return v

T["fr"] = _fr_typo(T["fr"])
LAB["fr"]["sent"] = LAB["fr"]["sent"]

LI_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v13M6 12l6 6 6-6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
SPARK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z"/></svg>'
X_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'

e = html.escape


def lab_html(lang, t):
    words, n = [], 0
    for i, tok in enumerate(LAB[lang]["said"].split(" ")):
        if "|" in tok:
            w, k = tok.rsplit("|", 1)
            words.append(f'<span class="w x" data-k="{k}" data-n="{n}"><s>{e(w)}</s></span>')
            n += 1
        else:
            words.append(f'<span class="w">{e(tok)}</span>')
    used = []
    for tok in LAB[lang]["said"].split(" "):
        if "|" in tok and tok[-1] not in used:
            used.append(tok[-1])
    tags = "".join(f'<li data-k="{k}"><span class="dot" aria-hidden="true"></span>{e(t["tags"][k])}</li>' for k in used)
    return " ".join(words), n, tags


def video(name, w, h, label, cls="", eager=False):
    return (f'<video class="vid {cls}" width="{w}" height="{h}" style="aspect-ratio:{w}/{h}" muted loop playsinline '
            f'preload="{"metadata" if eager else "none"}" poster="{{A}}media/{name}-poster.webp" aria-label="{e(label)}" data-auto>'
            f'<source src="{{A}}media/{name}.webm" type="video/webm"><source src="{{A}}media/{name}.mp4" type="video/mp4"></video>')


def page(lang):
    t = T[lang]
    A = "../assets/" if lang == "fr" else "assets/"
    url = BASE + ("fr/" if lang == "fr" else "")
    other = "../" if lang == "fr" else "fr/"
    said, n_removed, tags = lab_html(lang, t)
    lab = LAB[lang]
    pct = round((lab["tok_in"] - lab["tok_out"]) * 100 / lab["tok_in"])
    facts = [f.format(i=lab["tok_in"], o=lab["tok_out"], n=n_removed, s=lab["secs"]) for f in t["c3_facts"]]
    guide_data = {k: [v[0], v[1]] for k, v in t["guide"].items()}
    cfg = {"dl": DOWNLOAD_URL, "li": LINKEDIN}

    def dl_btn(cls="btn btn-primary", label=None):
        return f'<a class="{cls}" href="#telecharger" data-download><span>{e(label or t["dl_long"])}</span>{ARROW}</a>'

    nav = "".join(f'<a href="{h}">{e(l)}</a>' for h, l in t["nav"])
    pill_words = "".join(f'<span>{e(w)} </span>' for w in t["pill_words"].split(" "))
    h1 = "".join(f'<span class="line"><span class="line-in" style="--i:{i}">{e(l)}</span></span>' for i, l in enumerate(t["h1"]))
    meta = "".join(f"<li>{e(m)}</li>" for m in t["hero_meta"])
    clips = "".join(
        f'<figure class="clip" data-reveal style="--d:{i}"><div class="clip-frame">{video(n, w, h, c)}</div><figcaption>{e(c)}</figcaption></figure>'
        for i, (n, w, h, c) in enumerate(t["clips"]))
    steps = "".join(
        f'<li class="step" data-step="{i}"><span class="step-n" aria-hidden="true">{i+1}</span><div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>'
        for i, (a, b) in enumerate(t["steps"]))
    proof = "".join(f'<li data-reveal style="--d:{i}"><h3>{e(a)}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(t["proof"]))
    tiers = "".join(
        f'<li class="tier" style="--i:{i}"><img src="{A}brand/{"tier-original" if k == "icon" else k}.webp" width="384" height="384" alt="" loading="lazy" decoding="async"><span>{e(l)}</span></li>'
        for i, (k, l) in enumerate(t["tiers"]))
    fcols = "".join(
        f'<nav class="f-col" aria-label="{e(h)}"><h2>{e(h)}</h2><ul>' + "".join(f'<li><a href="{u}">{e(l)}</a></li>' for u, l in links) + "</ul></nav>"
        for h, links in t["f_cols"])
    mailto = f'mailto:{MAIL}?subject={quote(t["g3_mail_subject"])}&amp;body={quote(t["g3_mail_body"])}'
    soon = "" if DOWNLOAD_URL else f'<p class="soon"><span class="soon-dot" aria-hidden="true"></span>{e(t["soon"])}</p>'
    banner = f'<div class="lang-banner" hidden><p>{t["fr_banner"]}</p><button type="button" class="lang-banner-x" aria-label="{e(t["close"])}">{X_SVG}</button></div>' if t["fr_banner"] else ""

    out = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="theme-color" content="#062a21">
<meta name="color-scheme" content="dark light">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE}">
<link rel="alternate" hreflang="fr" href="{BASE}fr/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<link rel="icon" type="image/png" sizes="32x32" href="{A}favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{A}favicon-64.png">
<link rel="apple-touch-icon" href="{A}brand/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Better Vibe">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/og-{lang}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{t["alt_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(t["title"])}">
<meta name="twitter:description" content="{e(t["desc"])}">
<meta name="twitter:image" content="{BASE}assets/og-{lang}.jpg">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Better Vibe", "operatingSystem": "macOS 13 or later", "applicationCategory": "DeveloperApplication", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}, "description": t["desc"], "url": url, "inLanguage": lang, "author": {"@type": "Organization", "name": "Connected Mate"}}, ensure_ascii=False)}</script>
<link rel="preload" href="{A}fonts/montserrat-extrabold-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{A}brand/icon-640.webp" as="image" type="image/webp">
<link rel="stylesheet" href="{A}home.css">
<script>document.documentElement.classList.add("js");try{{if(matchMedia("(prefers-reduced-motion: reduce)").matches||/[?&]calm/.test(location.search))document.documentElement.classList.add("rm")}}catch(e){{}}</script>
<script src="{A}home.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{e(t["skip"])}</a>
{banner}
<div class="progress" aria-hidden="true"><span></span></div>
<header class="top">
  <a class="brand" href="./" aria-label="Better Vibe">
    <img src="{A}brand/icon-384.webp" alt="" width="36" height="36"><span>Better Vibe</span>
  </a>
  <nav class="top-nav" aria-label="{e("Principale" if lang == "fr" else "Main")}">{nav}</nav>
  <div class="top-actions">
    <a class="lang" href="{other}" hreflang="{"en" if lang == "fr" else "fr"}" aria-label="{e(t["lang_switch_label"])}">{t["lang_switch"]}</a>
    {dl_btn("btn btn-sm", t["dl"])}
  </div>
</header>

<main id="main">

<section class="hero" data-guide="hero" aria-labelledby="hero-h">
  <div class="hero-glow" aria-hidden="true"></div>
  <div class="hero-copy">
    <p class="kicker hero-in" style="--i:0">{e(t["hero_eyebrow"])}</p>
    <h1 id="hero-h" class="display">{h1}</h1>
    <p class="lede hero-in" style="--i:3">{e(t["lede"])}</p>
    <div class="cta-row hero-in" style="--i:4">
      {dl_btn()}
      <a class="btn btn-ghost" href="#produit">{e(t["see_demo"])}</a>
    </div>
    <ul class="hero-meta hero-in" style="--i:5">{meta}</ul>
    {soon}
  </div>
  <div class="hero-stage" role="img" aria-label="{e(t["hero_stage_label"])}">
    <div class="stage-icon" aria-hidden="true">
      <img src="{A}brand/icon-640.webp" width="640" height="640" alt="" fetchpriority="high">
    </div>
    <div class="stage-ui" aria-hidden="true">
      <div class="pill-text"><p>{pill_words}</p></div>
      <div class="pill"><i></i><span>{e(t["pill_listen"])}</span><b>.</b><b>.</b></div>
      <div class="result">
        <div class="result-top"><span class="result-title">{SPARK}{e(t["panel_title"])}</span><span class="result-copied">{CHECK}{e(t["panel_copied"])}</span></div>
        <p>{e(t["panel_text"])}</p>
      </div>
    </div>
  </div>
  <a class="scroll-cue" href="#vitesse"><span>{e(t["scroll"])}</span><i aria-hidden="true"></i></a>
</section>

<section id="vitesse" class="ch ch-speed pin" data-scrub="speed" data-guide="c1" aria-labelledby="c1-h">
  <div class="sticky">
    <div class="wrap">
      <p class="kicker">{e(t["c1_k"])}</p>
      <h2 id="c1-h" class="display-2">{e(t["c1_h"])}</h2>
      <p class="sub">{e(t["c1_p"])}</p>
      <div class="race" aria-hidden="true">
        <div class="lane lane-kb"><span class="lane-l">{e(t["c1_kb"])}</span><div class="lane-track"><p class="lane-text"><span>{e(t["c1_line"])}</span></p><i class="caret"></i></div></div>
        <div class="lane lane-voice"><span class="lane-l">{e(t["c1_voice"])}</span><div class="lane-track"><p class="lane-text"><span>{e(t["c1_line"])}</span></p><i class="caret"></i></div><span class="x3">×3</span></div>
      </div>
      <p class="src"><a href="{SPEECH_STUDY}" rel="noopener" target="_blank">{e(t["c1_src"])}<span class="vh"> {e(t["new_tab"])}</span></a></p>
    </div>
  </div>
</section>

<section id="nettoyage" class="ch ch-clean pin" data-scrub="clean" data-guide="c2" aria-labelledby="c2-h">
  <div class="sticky">
    <div class="wrap">
      <p class="kicker">{e(t["c2_k"])}</p>
      <h2 id="c2-h" class="display-2">{e(t["c2_h"])}</h2>
      <div class="lab">
        <div class="lab-meter"><span><b class="tok-in" data-from="{lab["tok_in"]}" data-to="{lab["tok_out"]}">{lab["tok_out"]}</b> {e(t["c2_tok_sent"])}</span><span class="tok-was">≈ {lab["tok_in"]} {e(t["c2_tok_said"])}</span><span class="tok-delta">−{lab["tok_in"] - lab["tok_out"]} tokens</span></div>
        <div class="lab-cols">
          <div class="lab-said"><h3>{e(t["c2_said"])}</h3><p>{said}</p></div>
          <div class="lab-sent"><h3>{e(t["c2_sent"])}</h3><p>{lab["sent"]}</p></div>
        </div>
        <div class="lab-why"><h3>{e(t["c2_why"])}</h3><ul>{tags}</ul></div>
      </div>
      <p class="note">{e(t["c2_note"])}</p>
    </div>
  </div>
</section>

<section id="tokens" class="ch ch-tokens" data-guide="c3" aria-labelledby="c3-h">
  <div class="wrap tokens-grid">
    <div>
      <p class="kicker">{e(t["c3_k"])}</p>
      <h2 id="c3-h" class="big-num"><span class="num" data-count="{pct}">−{pct}</span><span class="pct">%</span><span class="vh"> {e(t["c3_unit"])} {e(t["c3_sub"])}</span></h2>
      <p class="big-sub" aria-hidden="true">{e(t["c3_unit"])} <em>{e(t["c3_sub"])}</em></p>
    </div>
    <div>
      <p class="sub">{e(t["c3_p"])}</p>
      <ul class="facts">{"".join(f'<li data-reveal style="--d:{i}">{e(f)}</li>' for i, f in enumerate(facts))}</ul>
    </div>
  </div>
  <div class="ticker" aria-hidden="true"><div class="ticker-in">{"".join(f"<span>{e(w)}</span>" for w in (["euh", "du coup", "en fait", "genre", "voilà", "enfin bref", "non attends"] if lang == "fr" else ["uh", "like", "you know", "basically", "so yeah", "I mean", "no wait"]) * 2)}</div></div>
</section>

<section id="produit" class="ch ch-product" data-guide="c4" aria-labelledby="c4-h">
  <div class="wrap">
    <p class="kicker">{e(t["c4_k"])}</p>
    <h2 id="c4-h" class="display-2">{e(t["c4_h"])}</h2>
  </div>
  <div class="tour" data-scrub="tour" data-mode="view">
    <div class="mac">
      <div class="mac-screen">{video(t["c4_tour"], 1040, 700, t["c4_tour_label"], eager=True)}</div>
    </div>
  </div>
  <div class="wrap clips">{clips}</div>
</section>

<section id="comment" class="ch ch-how" data-guide="c5" aria-labelledby="c5-h">
  <div class="wrap how-grid">
    <div class="how-copy">
      <p class="kicker">{e(t["c5_k"])}</p>
      <h2 id="c5-h" class="display-2">{e(t["c5_h"])}</h2>
      <ol class="steps">{steps}</ol>
    </div>
    <div class="how-stage" aria-hidden="true">
      <div class="how-view" data-view="0"><img src="{A}media/{t["panel_img"]}.webp" width="340" height="510" alt="" loading="lazy" decoding="async"></div>
      <div class="how-view" data-view="1"><div class="clip-frame">{video("live-text-fr-light", 524, 198, t["clips"][0][3])}</div></div>
      <div class="how-view" data-view="2"><div class="clip-frame">{video("reveal-clean-fr", 520, 300, t["clips"][1][3])}</div></div>
      <div class="how-view" data-view="3">
        <div class="paste">
          <div class="paste-bar"><i></i><i></i><i></i><span>{e(t["paste_app"])}</span></div>
          <div class="paste-body"><p class="paste-text">{lab["sent"]}</p></div>
          <div class="paste-keys"><kbd>⌘</kbd><kbd>V</kbd></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="prive" class="ch ch-private" data-guide="c6" aria-labelledby="c6-h">
  <div class="wrap private-grid">
    <div class="vault" aria-hidden="true">
      <div class="vault-ring r1"></div><div class="vault-ring r2"></div><div class="vault-ring r3"></div>
      <div class="vault-core"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="10" rx="2.5"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>
      <div class="vault-wave">{"".join(f'<i style="--i:{i}"></i>' for i in range(9))}</div>
    </div>
    <div>
      <p class="kicker">{e(t["c6_k"])}</p>
      <h2 id="c6-h" class="display-2">{e(t["c6_h"])}</h2>
      <p class="sub">{e(t["c6_p"])}</p>
      <ul class="proof">{proof}</ul>
    </div>
  </div>
</section>

<section id="niveaux" class="ch ch-levels pin" data-scrub="levels" data-guide="c7" aria-labelledby="c7-h">
  <div class="sticky">
    <div class="wrap">
      <p class="kicker">{e(t["c7_k"])}</p>
      <h2 id="c7-h" class="display-2">{e(t["c7_h"])}</h2>
      <p class="sub">{e(t["c7_p"])}</p>
    </div>
    <ul class="tiers" aria-label="{e(", ".join(l for _, l in t["tiers"]))}">{tiers}</ul>
  </div>
</section>

<section id="telecharger" class="ch ch-end" data-guide="end" aria-labelledby="end-h">
  <div class="confetti" aria-hidden="true">{"".join(f'<i style="--i:{i}"></i>' for i in range(14))}</div>
  <div class="wrap end-in">
    <img class="end-mascot" src="{A}brand/mascot-celebrate.webp" width="256" height="256" alt="" loading="lazy" decoding="async">
    <h2 id="end-h" class="display-2">{e(t["end_h"])}</h2>
    <p class="sub">{e(t["end_p"])}</p>
    <div class="cta-row">{dl_btn()}</div>
    {soon}
    <p class="req">{e(t["end_req"])}</p>
  </div>
</section>

</main>

<aside class="guide" aria-label="{e(t["guide_label"])}" data-lines='{e(json.dumps(guide_data, ensure_ascii=False))}' data-base="{A}brand/">
  <div class="guide-bubble"><p class="guide-say">{e(t["guide"]["hero"][1])}</p></div>
  <img class="guide-img" src="{A}brand/mascot-happy.webp" width="256" height="256" alt="">
  <button type="button" class="guide-x" aria-label="{e(t["guide_hide"])}" data-hide="{e(t["guide_hide"])}" data-show="{e(t["guide_show"])}">{X_SVG}</button>
</aside>

<footer class="foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <a class="brand" href="./"><img src="{A}brand/icon-384.webp" alt="" width="44" height="44" loading="lazy"><span>Better Vibe</span></a>
      <p>{e(t["f_tag"])}</p>
      {dl_btn("btn btn-primary btn-sm", t["dl_long"])}
    </div>
    {fcols}
    <a class="li-card" href="{LINKEDIN}" rel="noopener" target="_blank">
      <span class="li-k">{e(t["f_li_k"])}</span>
      <span class="li-h">{LI_SVG}{e(t["f_li_h"])}</span>
      <span class="li-p">{e(t["f_li_p"])}</span>
      <span class="vh">{e(t["new_tab"])}</span>
    </a>
  </div>
  <div class="wordmark" aria-hidden="true">
    <span>Better Vibe</span>
    <img class="wordmark-mascot" src="{A}brand/mascot-happy.webp" width="256" height="256" alt="" loading="lazy" decoding="async">
  </div>
  <div class="wrap foot-bottom">
    <p>© 2026 {e(t["f_by"])}</p>
    <div class="foot-links"><a href="{other}" hreflang="{"en" if lang == "fr" else "fr"}">{e(t["lang_switch_label"])}</a><a href="#main">{e(t["f_top"])} ↑</a></div>
  </div>
</footer>

<dialog class="gate" aria-labelledby="gate-h" data-cfg='{e(json.dumps(cfg))}'>
  <button type="button" class="gate-x" data-close aria-label="{e(t["close"])}">{X_SVG}</button>
  <div class="gate-step" data-step="ask">
    <img class="gate-mascot" src="{A}brand/mascot-encourage.webp" width="256" height="256" alt="" loading="lazy">
    <h2 id="gate-h">{e(t["g1_h"])}</h2>
    <p>{e(t["g1_p"])}</p>
    <div class="gate-actions">
      <a class="btn btn-li" href="{LINKEDIN}" rel="noopener" target="_blank" data-follow>{LI_SVG}<span>{e(t["g1_follow"])}</span><span class="vh"> {e(t["new_tab"])}</span></a>
      <button type="button" class="gate-skip" data-skip>{e(t["g1_skip"])}&nbsp;→</button>
    </div>
  </div>
  <div class="gate-step" data-step="go" hidden>
    <img class="gate-mascot" src="{A}brand/mascot-celebrate.webp" width="256" height="256" alt="" loading="lazy">
    <h2 tabindex="-1"><span class="thanks">{e(t["g2_h_thanks"])}</span><span class="nothanks">{e(t["g2_h"])}</span></h2>
    <p>{e(t["g2_p"])}</p>
    <div class="gate-actions"><a class="btn btn-primary" href="{e(DOWNLOAD_URL or "#telecharger")}" data-go><span>{e(t["g2_go"])}</span>{ARROW}</a></div>
  </div>
  <div class="gate-step" data-step="soon" hidden>
    <img class="gate-mascot" src="{A}brand/mascot-streak.webp" width="256" height="256" alt="" loading="lazy">
    <h2 tabindex="-1"><span class="thanks">{e(t["g2_h_thanks"])} </span>{e(t["g3_h"])}</h2>
    <p>{e(t["g3_p"])}</p>
    <div class="gate-actions">
      <a class="btn btn-primary" href="{mailto}"><span>{e(t["g3_mail"])}</span></a>
      <a class="btn btn-ghost-dark" href="{LINKEDIN}" rel="noopener" target="_blank">{LI_SVG}<span>{e(t["g3_li"])}</span><span class="vh"> {e(t["new_tab"])}</span></a>
      <button type="button" class="gate-skip" data-close>{e(t["close"])}</button>
    </div>
  </div>
</dialog>
</body>
</html>
'''
    return out.replace("{A}", A)
