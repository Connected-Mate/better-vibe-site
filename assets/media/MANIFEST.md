# Better Vibe media manifest

Captured 2026-10-28 from repo HEAD (v1.2.2, Debug build, clean git export; uncommitted edits excluded). Real app UI rendered by the app's own demo flags; window-only capture (no desktop, no other apps). Capture display is 1x: all stills are native pixels (no true 2x/retina variants exist; none faked). No personal history shown (History/Settings screens intentionally NOT captured). Home screens show demo-machine stats (level 3, a few prompts).

Caveats: reveal clip shows the banner 'Nettoyage léger seulement — Apple Intelligence est désactivé' (AI off on capture Mac) before the level-up/score frame; long/skipped reveal stills use canned French text (FR only). Videos were captured at about 12 fps and encoded at 24 fps (frame-duplicated); no audio. Reveal panel is always dark (appearance-independent). Onboarding language step highlights the Mac's own language.

## Videos (mp4 H.264 yuv420p faststart + webm VP9 + poster .webp/.jpg, same base name)
| base | shows | px | sec | mp4 B | webm B | lang | look |
|---|---|---|---|---|---|---|---|
| app-tour-fr-light | Main window tour: home, Dictate, How it works, Lab | 1040x700 | 10.9 | 526911 | 482522 | FR | light |
| app-tour-en-dark | Main window tour: home, Dictate, How it works, Lab | 1040x700 | 11.1 | 472218 | 422502 | EN | dark |
| reveal-clean-fr | Result panel: messy dictation -> clean prompt, score 63 (trimmed 4.3–7.85 s of the raw capture to drop the "Apple Intelligence désactivé" banner, last frame held 1.8 s) | 520x300 | 5.4 | 61900 | 52499 | FR | dark panel |
| live-text-fr-light | Menu-bar pill 'Écoute..' with live words appearing while speaking | 524x198 | 11.8 | 71381 | 79058 | FR | light-desktop |
| onboarding-fr-light | Onboarding tour, welcome through personalisation | 822x620 | 12.2 | 332364 | 284183 | FR | light |

## Stills (.webp q82, native 1x pixels)
| file | px | bytes |
|---|---|---|
| still-about-en-dark.webp | 1040x700 | 36160 |
| still-about-en-light.webp | 1040x700 | 37848 |
| still-about-fr-dark.webp | 1040x700 | 37228 |
| still-about-fr-light.webp | 1040x700 | 38652 |
| still-dictate-en-dark.webp | 1040x700 | 35844 |
| still-dictate-en-light.webp | 1040x700 | 38542 |
| still-dictate-fr-dark.webp | 1040x700 | 39950 |
| still-dictate-fr-light.webp | 1040x700 | 42646 |
| still-dictate-rewritten-en-light.webp | 1040x700 | 35952 |
| still-dictate-rewritten-fr-light.webp | 1040x700 | 39438 |
| still-home-en-dark.webp | 1040x700 | 33808 |
| still-home-en-light.webp | 1040x700 | 34886 |
| still-home-fr-dark.webp | 1040x700 | 34968 |
| still-home-fr-light.webp | 1040x700 | 36154 |
| still-howItWorks-en-dark.webp | 1040x700 | 32714 |
| still-howItWorks-en-light.webp | 1040x700 | 35252 |
| still-howItWorks-fr-dark.webp | 1040x700 | 35286 |
| still-howItWorks-fr-light.webp | 1040x700 | 37934 |
| still-lab-en-dark.webp | 1040x700 | 28408 |
| still-lab-en-light.webp | 1040x700 | 30158 |
| still-lab-fr-dark.webp | 1040x700 | 30718 |
| still-lab-fr-light.webp | 1040x700 | 33000 |
| still-lab-result-en-light.webp | 1040x700 | 37554 |
| still-lab-result-fr-light.webp | 1040x700 | 43456 |
| still-livetext-long-en-dark.webp | 548x222 | 8556 |
| still-livetext-long-fr-dark.webp | 548x222 | 8746 |
| still-livetext-pill-en-dark.webp | 548x222 | 4038 |
| still-livetext-pill-en-light.webp | 548x222 | 4252 |
| still-livetext-pill-fr-dark.webp | 548x222 | 5134 |
| still-livetext-pill-fr-light.webp | 548x222 | 5464 |
| still-menubar-panel-fr-dark.webp | 340x510 | 19386 |
| still-menubar-panel-fr-light.webp | 340x510 | 19038 |
| still-menubar-voicemodel-fr-dark.webp | 340x574 | 19410 |
| still-menubar-voicemodel-fr-light.webp | 340x574 | 20606 |
| still-onboarding-0-en-dark.webp | 820x620 | 18876 |
| still-onboarding-0-en-light.webp | 820x620 | 19978 |
| still-onboarding-0-fr-dark.webp | 820x620 | 20436 |
| still-onboarding-0-fr-light.webp | 820x620 | 21658 |
| still-onboarding-1-en-dark.webp | 820x620 | 30442 |
| still-onboarding-1-en-light.webp | 820x620 | 33504 |
| still-onboarding-1-fr-dark.webp | 820x620 | 33528 |
| still-onboarding-1-fr-light.webp | 820x620 | 35476 |
| still-onboarding-2-en-dark.webp | 820x620 | 28134 |
| still-onboarding-2-en-light.webp | 820x620 | 29266 |
| still-onboarding-2-fr-dark.webp | 820x620 | 29270 |
| still-onboarding-2-fr-light.webp | 820x620 | 30562 |
| still-onboarding-3-en-dark.webp | 820x620 | 21906 |
| still-onboarding-3-en-light.webp | 820x620 | 23352 |
| still-onboarding-3-fr-dark.webp | 820x620 | 23328 |
| still-onboarding-3-fr-light.webp | 820x620 | 24870 |
| still-onboarding-4-en-dark.webp | 820x620 | 23306 |
| still-onboarding-4-en-light.webp | 820x620 | 23488 |
| still-onboarding-4-fr-dark.webp | 820x620 | 23848 |
| still-onboarding-4-fr-light.webp | 820x620 | 24212 |
| still-onboarding-5-en-dark.webp | 820x620 | 22660 |
| still-onboarding-5-en-light.webp | 820x620 | 23200 |
| still-onboarding-5-fr-dark.webp | 820x620 | 24686 |
| still-onboarding-5-fr-light.webp | 820x620 | 25124 |
| still-onboarding-6-en-dark.webp | 820x620 | 28276 |
| still-onboarding-6-en-light.webp | 820x620 | 29982 |
| still-onboarding-6-fr-dark.webp | 820x620 | 30628 |
| still-onboarding-6-fr-light.webp | 820x620 | 32340 |
| still-reveal-levelup-en.webp | 540x340 | 14832 |
| still-reveal-levelup-fr.webp | 540x340 | 15304 |
| still-reveal-long-fr.webp | 540x504 | 31518 |
| still-reveal-routine-en.webp | 540x272 | 11518 |
| still-reveal-routine-fr.webp | 540x276 | 12538 |
| still-reveal-skipped-fr.webp | 540x380 | 25164 |

Name key: home/dictate/howItWorks/about/lab = main window sections; dictate-rewritten = Dictate with a messy dictation and its clean rewrite; lab-result = Lab rewrite with removed words struck; onboarding-0..6 = welcome, how it works, mic, language, voice model, try it, make it yours; reveal-* = result panel (routine, levelup with score, long brief, skipped); livetext-pill = live words pill; menubar-panel / menubar-voicemodel = menu-bar panel and its voice model picker (demo history entries).
