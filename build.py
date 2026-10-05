#!/usr/bin/env python3
"""Generates EN (root) and FR (/fr/) pages. Run: python3 build.py"""
import os, html

BASE = "https://connected-mate.github.io/better-vibe-site/"
STORE = "https://apps.apple.com/us/search?term=Better%20Vibe"
MAIL = "alex.connectedmate@gmail.com"
ISSUES = "https://github.com/Connected-Mate/better-vibe-site/issues"
ROOT = os.path.dirname(os.path.abspath(__file__))

APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.37 1.43c0 1.14-.46 2.22-1.2 3-.78.84-2.06 1.5-3.1 1.41-.13-1.1.4-2.25 1.14-3 .83-.87 2.2-1.5 3.16-1.41zM20.5 17.1c-.55 1.27-.81 1.83-1.52 2.95-.99 1.56-2.39 3.5-4.12 3.51-1.54.02-1.94-1-4.03-.99-2.09.01-2.53 1.01-4.07.99-1.73-.02-3.05-1.77-4.04-3.33C-.2 15.94-.49 10.8 1.23 8.14c1.22-1.89 3.15-2.99 4.96-2.99 1.84 0 3 1.01 4.52 1.01 1.48 0 2.38-1.01 4.51-1.01 1.61 0 3.32.88 4.54 2.4-3.99 2.19-3.34 7.88.74 9.55z"/></svg>'

T = {
"en": {
 "lang":"en","dir":"", "other":"fr","other_label":"Français","other_name":"Français",
 "skip":"Skip to content","nav_home":"Home","nav_support":"Support","nav_privacy":"Privacy",
 "app_tagline":"Voice to prompt, 100% offline",
 "title_home":"Better Vibe — Speak. Your prompt is ready.",
 "desc_home":"Better Vibe is a Mac menu-bar app: press a shortcut, talk, and a clean prompt for your AI coding assistant lands on your clipboard. 100% on-device. No account, no tracking.",
 "h1":"Speak. Your prompt is ready.",
 "lede":"Press a shortcut and say what you want, \"uh\"s and all. Better Vibe turns it into a clean prompt for your coding assistant, with your clipboard attached as context. Your voice never leaves your Mac.",
 "cta":"Download on the Mac App Store","cta_note":"For Mac with Apple Silicon, macOS 13 or later.",
 "mock_title":"Better Vibe — result",
 "mock_said_l":"What you said",
 "mock_said":"“euh so the retry logic is duplicated in like three places, pull it into one function, no wait, one actor.”",
 "mock_out_l":"What lands on your clipboard",
 "mock_out":"<b>## Task</b>\nRefactor the retry logic into a single actor. It is currently duplicated in three places.\n\n<b>## Context</b>\n```swift\n// your copied code, fenced\n```",
 "lv":["Raw","Cleaned","Structured","AI Polish"],"lv_on":2,
 "video_label":"Better Vibe in 30 seconds",
 "how_eyebrow":"How it works","how_h":"Four steps. No typing.",
 "steps":[
  ("Copy what you're working on","The code, the error or the link. <kbd>⌘C</kbd>, like always."),
  ("Press the shortcut and talk","<kbd>⌘⇧D</kbd> by default. Say it like you'd tell a colleague. Hesitations are fine."),
  ("Press it again","Better Vibe transcribes locally, removes the filler, resolves your self-corrections and attaches your clipboard as properly formatted context."),
  ("Paste anywhere","<kbd>⌘V</kbd> into any chat, IDE or terminal. It works with any AI assistant that has a text box."),
 ],
 "priv_eyebrow":"Private by architecture","priv_h":"Your voice stays on your Mac.",
 "priv_p":"Transcription, cleanup and prompt assembly all run on your Mac. There is no account, no analytics and no tracking.",
 "proof":[
  ("Local Whisper","Speech recognition runs on-device with Metal acceleration. Audio is never transmitted."),
  ("One optional download","The only network use: fetching Whisper model files from Hugging Face, when you ask for it."),
  ("No data collected","The App Store label reads “No Data Collected”. Read the full <a href=\"{priv}\">privacy policy</a>."),
 ],
 "feat_eyebrow":"Features","feat_h":"Made for how you actually speak",
 "feats":[
  ("Four improvement levels","Raw, Cleaned, Structured, or AI Polish. Switch between them with the arrow keys right on the result window."),
  ("AI Polish, on-device","On Macs with Apple Intelligence (macOS 26 or later), Apple's on-device model rewrites your dictation as a precise instruction. Optional, and it falls back to the local cleanup when unavailable."),
  ("Context that formats itself","Swift, TypeScript, Python, JSON, URLs, error logs, file paths: each is detected and fenced correctly. Pin extra snippets when one clipboard isn't enough."),
  ("Prompt templates","Fix a bug, build a feature, refactor, code review, explain, commit message, or free-form. Markdown or XML output."),
  ("Still a full dictation app","Dictate to clipboard, 17 languages with auto-detect, voice commands for punctuation, a custom dictionary and an optional profanity filter."),
  ("Built for Apple Silicon","Whisper models from Tiny (fast) to Large v3 (most accurate). Better Vibe recommends one based on your chip, memory and measured speed."),
 ],
 "req_eyebrow":"Requirements","req_h":"What you need",
 "reqs":["A Mac with Apple Silicon (M1 or later)","macOS 13 Ventura or later","Microphone access, the only permission the app asks for","macOS 26 with Apple Intelligence for the optional AI Polish level"],
 "foot_by":"Better Vibe by Connected Mate.",
 "foot_contact":"Contact",
 # privacy
 "title_priv":"Privacy Policy — Better Vibe","desc_priv":"Better Vibe collects no data. Your voice is processed on your Mac and never transmitted. Read the full privacy policy.",
 "p_h1":"Privacy Policy","p_meta":"Effective date: October 5, 2026",
 "p_toc":"On this page",
 "p_secs":[
  ("summary","Summary",["<p>Better Vibe collects no data of any kind. It has no account system, no analytics, no advertising and no third-party SDKs. Everything the app does with your voice and your text happens on your Mac.</p>"]),
  ("audio","Microphone and audio",["<p>Better Vibe asks for microphone access so it can transcribe your dictation. Audio is processed on your Mac by Whisper, running locally. It is never transmitted to us or to anyone else, A copy of the recording is kept on your Mac only until transcription succeeds, so a failed dictation can be retried; it is then deleted.</p><p>If you choose a screenshots folder in the settings, the app notes the file names of screenshots you take during a dictation so it can mention them in your prompt. The images are never opened or sent anywhere.</p>"]),
  ("network","Network activity",["<p>The app makes a single kind of network connection: when you choose to download a Whisper speech model, the file is fetched over HTTPS from Hugging Face (huggingface.co). Like any download from a website, this reveals your IP address to Hugging Face, which is subject to <a href=\"https://huggingface.co/privacy\" rel=\"noopener\">its own privacy policy</a>. No audio, transcription, prompt, usage data or identifier is sent as part of this download.</p>","<p>If you never download a model, or use the app offline once a model is installed, the app makes no network connection at all.</p>"]),
  ("clipboard","Clipboard",["<p>Better Vibe reads your clipboard only when you trigger a dictation, in order to attach it to your prompt as context. It writes the finished prompt back to the clipboard. Clipboard contents are processed on your Mac and never leave it. The app does not read your clipboard in the background.</p>"]),
  ("local","Data stored on your Mac",["<p>The following stays on your device, in the app's own data folder, and is never sent anywhere:</p>","<ul><li>your settings, shortcuts and custom dictionary;</li><li>the downloaded Whisper models;</li><li>a local history and diagnostic log of recent dictations, kept to help the app improve the quality of your results on your own Mac.</li></ul>","<p>You can delete this history from within the app, and removing the app's data folder erases everything the app has stored. Uninstalling the app and its data folder leaves nothing behind.</p>"]),
  ("ai","Apple Intelligence",["<p>The optional AI Polish level uses Apple's on-device model on macOS 26 or later. It runs entirely on your Mac. When it is unavailable, the app uses a local rule-based cleanup instead.</p>"]),
  ("store","Mac App Store",["<p>Better Vibe is distributed through the Mac App Store. Apple may process information about your download and purchase under Apple's own privacy policy. We receive no personal information from Apple about you.</p>"]),
  ("children","Children",["<p>Better Vibe is rated 4+ and collects no personal information from anyone, including children.</p>"]),
  ("changes","Changes to this policy",["<p>If this policy changes, we will update the effective date above and publish the new version on this page. Because the app collects no data, we expect changes to be rare.</p>"]),
  ("contact","Contact",["<p>Questions about privacy? Write to <a href=\"mailto:%s\">%s</a>. Better Vibe is developed by Connected Mate.</p>" % (MAIL, MAIL)]),
 ],
 # support
 "title_supp":"Support — Better Vibe","desc_supp":"Help for Better Vibe: microphone permission, shortcuts, model download, offline use, Apple Intelligence, troubleshooting, and how to contact us.",
 "s_h1":"Support","s_lede":"Quick answers first. If you're still stuck, write to us.",
 "faq_h":"Frequently asked questions",
 "faqs":[
  ("The app can't hear me. How do I allow the microphone?","<p>Open <strong>System Settings → Privacy &amp; Security → Microphone</strong> and switch Better Vibe on. If it isn't listed, quit and reopen the app and start a dictation again so macOS asks. Also check that the right input is selected in <strong>System Settings → Sound → Input</strong>.</p>"),
  ("What is the shortcut, and can I change it?","<p>By default <kbd>⌘⇧D</kbd> starts and stops a prompt dictation, <kbd>⌘⇧C</kbd> dictates straight to the clipboard, and <kbd>⌘⇧N</kbd> cycles your languages. All shortcuts can be changed in the app's Settings. If a shortcut does nothing, another app may be using the same combination: pick a different one.</p>"),
  ("How do I download a speech model?","<p>On first launch, the onboarding lets you pick a Whisper model, and Better Vibe recommends one for your Mac. You can download others later in Settings. Models are fetched from Hugging Face over HTTPS, so you need an internet connection for that step only. Larger models are more accurate but take more space and time.</p>"),
  ("Does it work offline?","<p>Yes. Once a model is downloaded, transcription, cleanup and prompt assembly work with no internet connection at all.</p>"),
  ("What does AI Polish need?","<p>AI Polish is optional and requires macOS 26 or later on a Mac with Apple Intelligence enabled (<strong>System Settings → Apple Intelligence &amp; Siri</strong>). If it isn't available, Better Vibe automatically uses its local cleanup instead, so you always get a result.</p>"),
  ("Where does my prompt go? Nothing was pasted.","<p>Better Vibe never pastes for you. The prompt is placed on your clipboard and shown in a result window: press <kbd>⌘V</kbd> in your assistant, editor or terminal.</p>"),
  ("The transcription is wrong or in the wrong language.","<p>Try a larger Whisper model, check your selected languages in Settings, speak a little closer to the microphone, and add unusual names or terms to the custom dictionary.</p>"),
  ("The shortcut starts but nothing happens afterwards.","<p>Press the shortcut a second time to stop the recording: it works as start/stop. Also check that a model is installed and the microphone permission is on.</p>"),
  ("Is my data collected?","<p>No. See the <a href=\"{priv}\">privacy policy</a>.</p>"),
 ],
 "contact_h":"Still need help?",
 "contact_p":"Email us and include your Mac model and macOS version.",
 "contact_issue":"Or open an issue on GitHub",
 "contact_issue_note":"(public: don't include private information)",
},
"fr": {
 "lang":"fr","other":"en","other_label":"English","other_name":"English",
 "skip":"Aller au contenu","nav_home":"Accueil","nav_support":"Assistance","nav_privacy":"Confidentialité",
 "app_tagline":"Parle. Ton prompt est prêt.",
 "title_home":"Better Vibe — Parle. Ton prompt est prêt.",
 "desc_home":"Better Vibe est une app Mac de barre de menus : un raccourci, tu parles, et un prompt propre pour ton assistant de code arrive dans ton presse-papiers. 100 % sur ton Mac. Sans compte, sans tracking.",
 "h1":"Parle. Ton prompt est prêt.",
 "lede":"Appuie sur un raccourci et dis ce que tu veux, avec tes « euh ». Better Vibe en fait un prompt propre pour ton assistant de code, avec ton presse-papiers joint comme contexte. Ta voix ne quitte jamais ton Mac.",
 "cta":"Télécharger sur le Mac App Store","cta_note":"Pour Mac Apple Silicon, macOS 13 ou plus récent.",
 "mock_title":"Better Vibe — résultat",
 "mock_said_l":"Ce que tu as dit",
 "mock_said":"« euh donc la logique de retry est dupliquée à trois endroits, mets-la dans une fonction, non attends, un acteur. »",
 "mock_out_l":"Ce qui arrive dans ton presse-papiers",
 "mock_out":"<b>## Tâche</b>\nRefactorer la logique de retry dans un seul acteur. Elle est actuellement dupliquée à trois endroits.\n\n<b>## Contexte</b>\n```swift\n// ton code copié, balisé\n```",
 "lv":["Brut","Nettoyé","Structuré","Retouche IA"],"lv_on":2,
 "video_label":"Better Vibe en 30 secondes",
 "how_eyebrow":"Comment ça marche","how_h":"Quatre étapes. Zéro frappe.",
 "steps":[
  ("Copie ce sur quoi tu travailles","Le code, l'erreur ou le lien. <kbd>⌘C</kbd>, comme d'habitude."),
  ("Appuie sur le raccourci et parle","<kbd>⌘⇧D</kbd> par défaut. Dis-le comme à un collègue. Les hésitations ne gênent pas."),
  ("Appuie à nouveau","Better Vibe transcrit en local, retire les tics de langage, résout tes corrections orales et joint ton presse-papiers comme contexte bien formaté."),
  ("Colle où tu veux","<kbd>⌘V</kbd> dans n'importe quel chat, IDE ou terminal. Ça marche avec tout assistant IA qui a un champ de texte."),
 ],
 "priv_eyebrow":"Privé par architecture","priv_h":"Ta voix reste sur ton Mac.",
 "priv_p":"Transcription, nettoyage et assemblage du prompt tournent sur ton Mac. Pas de compte, pas d'analytique, pas de tracking.",
 "proof":[
  ("Whisper en local","La reconnaissance vocale tourne sur ton Mac, accélérée par Metal. L'audio n'est jamais transmis."),
  ("Un seul téléchargement, optionnel","Le seul usage réseau : récupérer les modèles Whisper sur Hugging Face, quand tu le demandes."),
  ("Aucune donnée collectée","L'étiquette App Store indique « Aucune donnée collectée ». Lis la <a href=\"{priv}\">politique de confidentialité</a>."),
 ],
 "feat_eyebrow":"Fonctionnalités","feat_h":"Pensé pour ta façon de parler",
 "feats":[
  ("Quatre niveaux d'amélioration","Brut, Nettoyé, Structuré ou Retouche IA. Passe de l'un à l'autre avec les flèches, directement sur la fenêtre de résultat."),
  ("Retouche IA, sur ton Mac","Sur les Mac avec Apple Intelligence (macOS 26 et plus), le modèle local d'Apple reformule ta dictée en instruction précise. Optionnel, avec repli automatique sur le nettoyage local."),
  ("Un contexte qui se formate tout seul","Swift, TypeScript, Python, JSON, URL, logs d'erreur, chemins de fichiers : chacun est détecté et balisé correctement. Épingle d'autres extraits quand un seul presse-papiers ne suffit pas."),
  ("Templates de prompt","Corriger un bug, construire une fonctionnalité, refactorer, revue de code, expliquer, message de commit, ou format libre. Sortie en Markdown ou XML."),
  ("Toujours une vraie app de dictée","Dictée vers le presse-papiers, 17 langues avec détection auto, commandes vocales de ponctuation, dictionnaire personnalisé et filtre de grossièretés optionnel."),
  ("Conçu pour Apple Silicon","Modèles Whisper du Tiny (rapide) au Large v3 (le plus précis). Better Vibe en recommande un selon ta puce, ta mémoire et ta vitesse mesurée."),
 ],
 "req_eyebrow":"Prérequis","req_h":"Ce qu'il te faut",
 "reqs":["Un Mac Apple Silicon (M1 ou plus récent)","macOS 13 Ventura ou plus récent","L'accès au microphone, la seule autorisation demandée","macOS 26 avec Apple Intelligence pour le niveau optionnel Retouche IA"],
 "foot_by":"Better Vibe par Connected Mate.",
 "foot_contact":"Contact",
 "title_priv":"Politique de confidentialité — Better Vibe","desc_priv":"Better Vibe ne collecte aucune donnée. Ta voix est traitée sur ton Mac et jamais transmise. Lis la politique de confidentialité complète.",
 "p_h1":"Politique de confidentialité","p_meta":"Date d'entrée en vigueur : 5 octobre 2026",
 "p_toc":"Sur cette page",
 "p_secs":[
  ("summary","Résumé",["<p>Better Vibe ne collecte aucune donnée, d'aucune sorte. L'app n'a ni compte, ni analytique, ni publicité, ni SDK tiers. Tout ce que l'app fait avec ta voix et ton texte se passe sur ton Mac.</p>"]),
  ("audio","Microphone et audio",["<p>Better Vibe demande l'accès au microphone pour transcrire ta dictée. L'audio est traité sur ton Mac par Whisper, en local. Il n'est jamais transmis, ni à nous ni à quiconque, Une copie de l'enregistrement reste sur ton Mac seulement jusqu'à la fin de la transcription, pour pouvoir relancer une dictée qui a échoué ; elle est ensuite supprimée.</p><p>Si tu choisis un dossier de captures d'écran dans les réglages, l'app note le nom des captures prises pendant une dictée pour les mentionner dans ton prompt. Les images ne sont jamais ouvertes ni envoyées.</p>"]),
  ("network","Activité réseau",["<p>L'app n'établit qu'un seul type de connexion : quand tu choisis de télécharger un modèle vocal Whisper, le fichier est récupéré en HTTPS sur Hugging Face (huggingface.co). Comme pour tout téléchargement depuis un site web, cela révèle ton adresse IP à Hugging Face, qui applique <a href=\"https://huggingface.co/privacy\" rel=\"noopener\">sa propre politique de confidentialité</a>. Aucun audio, aucune transcription, aucun prompt, aucune donnée d'usage ni aucun identifiant n'est envoyé lors de ce téléchargement.</p>","<p>Si tu ne télécharges aucun modèle, ou si tu utilises l'app hors ligne une fois un modèle installé, l'app n'établit aucune connexion réseau.</p>"]),
  ("clipboard","Presse-papiers",["<p>Better Vibe lit ton presse-papiers uniquement quand tu déclenches une dictée, pour le joindre à ton prompt comme contexte. Elle y réécrit ensuite le prompt final. Le contenu est traité sur ton Mac et ne le quitte jamais. L'app ne lit pas ton presse-papiers en arrière-plan.</p>"]),
  ("local","Données stockées sur ton Mac",["<p>Ce qui suit reste sur ton appareil, dans le dossier de données de l'app, et n'est jamais envoyé nulle part :</p>","<ul><li>tes réglages, raccourcis et dictionnaire personnalisé ;</li><li>les modèles Whisper téléchargés ;</li><li>un historique local et un journal de diagnostic des dernières dictées, conservés pour améliorer la qualité de tes résultats sur ton propre Mac.</li></ul>","<p>Tu peux supprimer cet historique depuis l'app, et supprimer le dossier de données de l'app efface tout ce qu'elle a stocké. Désinstaller l'app et son dossier de données ne laisse rien derrière.</p>"]),
  ("ai","Apple Intelligence",["<p>Le niveau optionnel Retouche IA utilise le modèle local d'Apple sur macOS 26 ou plus récent. Il tourne entièrement sur ton Mac. Quand il n'est pas disponible, l'app utilise à la place un nettoyage local à règles.</p>"]),
  ("store","Mac App Store",["<p>Better Vibe est distribuée via le Mac App Store. Apple peut traiter des informations sur ton téléchargement et ton achat selon sa propre politique de confidentialité. Nous ne recevons d'Apple aucune information personnelle te concernant.</p>"]),
  ("children","Enfants",["<p>Better Vibe est classée 4+ et ne collecte aucune information personnelle, auprès de personne, enfants compris.</p>"]),
  ("changes","Modifications de cette politique",["<p>Si cette politique change, nous mettrons à jour la date d'entrée en vigueur ci-dessus et publierons la nouvelle version sur cette page. Comme l'app ne collecte aucune donnée, nous attendons peu de changements.</p>"]),
  ("contact","Contact",["<p>Une question sur la confidentialité ? Écris à <a href=\"mailto:%s\">%s</a>. Better Vibe est développée par Connected Mate.</p>" % (MAIL, MAIL)]),
 ],
 "title_supp":"Assistance — Better Vibe","desc_supp":"Aide pour Better Vibe : autorisation du micro, raccourcis, téléchargement du modèle, usage hors ligne, Apple Intelligence, dépannage et contact.",
 "s_h1":"Assistance","s_lede":"Les réponses rapides d'abord. Si tu es toujours bloqué, écris-nous.",
 "faq_h":"Questions fréquentes",
 "faqs":[
  ("L'app ne m'entend pas. Comment autoriser le micro ?","<p>Ouvre <strong>Réglages Système → Confidentialité et sécurité → Microphone</strong> et active Better Vibe. Si elle n'apparaît pas, quitte puis rouvre l'app et relance une dictée pour que macOS pose la question. Vérifie aussi l'entrée choisie dans <strong>Réglages Système → Son → Entrée</strong>.</p>"),
  ("Quel est le raccourci, et puis-je le changer ?","<p>Par défaut, <kbd>⌘⇧D</kbd> démarre et arrête une dictée de prompt, <kbd>⌘⇧C</kbd> dicte directement vers le presse-papiers et <kbd>⌘⇧N</kbd> fait défiler tes langues. Tous les raccourcis se changent dans les Réglages de l'app. Si un raccourci ne fait rien, une autre app utilise peut-être la même combinaison : choisis-en une autre.</p>"),
  ("Comment télécharger un modèle vocal ?","<p>Au premier lancement, l'accueil te propose un modèle Whisper, et Better Vibe en recommande un pour ton Mac. Tu peux en télécharger d'autres plus tard dans les Réglages. Les modèles viennent de Hugging Face en HTTPS : il te faut donc Internet pour cette étape seulement. Les gros modèles sont plus précis mais prennent plus de place et de temps.</p>"),
  ("Ça marche hors ligne ?","<p>Oui. Une fois un modèle téléchargé, transcription, nettoyage et assemblage du prompt fonctionnent sans aucune connexion Internet.</p>"),
  ("Que faut-il pour la Retouche IA ?","<p>La Retouche IA est optionnelle et demande macOS 26 ou plus récent sur un Mac avec Apple Intelligence activée (<strong>Réglages Système → Apple Intelligence et Siri</strong>). Si elle n'est pas disponible, Better Vibe utilise automatiquement son nettoyage local : tu as toujours un résultat.</p>"),
  ("Où va mon prompt ? Rien ne s'est collé.","<p>Better Vibe ne colle jamais à ta place. Le prompt est placé dans ton presse-papiers et affiché dans une fenêtre de résultat : appuie sur <kbd>⌘V</kbd> dans ton assistant, ton éditeur ou ton terminal.</p>"),
  ("La transcription est fausse ou dans la mauvaise langue.","<p>Essaie un modèle Whisper plus grand, vérifie les langues choisies dans les Réglages, rapproche-toi du micro, et ajoute les noms ou termes inhabituels au dictionnaire personnalisé.</p>"),
  ("Le raccourci démarre mais rien ne se passe ensuite.","<p>Appuie une seconde fois sur le raccourci pour arrêter l'enregistrement : il fonctionne en démarrage/arrêt. Vérifie aussi qu'un modèle est installé et que l'accès au micro est activé.</p>"),
  ("Mes données sont-elles collectées ?","<p>Non. Voir la <a href=\"{priv}\">politique de confidentialité</a>.</p>"),
 ],
 "contact_h":"Encore besoin d'aide ?",
 "contact_p":"Écris-nous en précisant ton modèle de Mac et ta version de macOS.",
 "contact_issue":"Ou ouvre un ticket sur GitHub",
 "contact_issue_note":"(public : n'y mets aucune information privée)",
},
}

def page_url(lang, name):
    return BASE + ("fr/" if lang == "fr" else "") + name

def head(t, lang, name, title, desc, asset):
    other = "en" if lang == "fr" else "fr"
    en_u, fr_u = page_url("en", name), page_url("fr", name)
    img = BASE + "assets/icon-512.png"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#f2f8f5" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#08201b" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{page_url(lang, name)}">
<link rel="alternate" hreflang="en" href="{en_u}">
<link rel="alternate" hreflang="fr" href="{fr_u}">
<link rel="alternate" hreflang="x-default" href="{en_u}">
<link rel="icon" type="image/png" sizes="32x32" href="{asset}favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{asset}favicon-64.png">
<link rel="apple-touch-icon" href="{asset}icon-256.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Better Vibe">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{page_url(lang, name)}">
<meta property="og:image" content="{img}">
<meta property="og:locale" content="{'fr_FR' if lang=='fr' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if lang=='fr' else 'fr_FR'}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{img}">
<link rel="preload" href="{asset}fonts/Montserrat-ExtraBoldItalic.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="{asset}style.css">
</head>
'''

def header(t, lang, name, asset, home, cur):
    # language switch
    sw = ("fr/" + name) if lang == "en" else ("../" + name)
    if lang == "fr" and name == "index.html":
        sw = "../"
    if lang == "en" and name == "index.html":
        sw = "fr/"
    def cur_attr(k): return ' aria-current="page"' if cur == k else ""
    return f'''<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="wrap site-head">
  <a class="brand" href="{home}" aria-label="Better Vibe, {t["nav_home"]}"><img src="{asset}icon-64.png" alt="" width="40" height="40">Better Vibe</a>
  <nav class="nav" aria-label="Main">
    <a href="{home}"{cur_attr("home")}>{t["nav_home"]}</a>
    <a href="support.html"{cur_attr("support")}>{t["nav_support"]}</a>
    <a href="privacy.html"{cur_attr("privacy")}>{t["nav_privacy"]}</a>
    <a class="lang" href="{sw}" hreflang="{t["other"]}" lang="{t["other"]}" aria-label="{t["other_name"]}">{t["other_label"]}</a>
  </nav>
</header>
'''

def footer(t):
    return f'''<footer>
  <div class="wrap">
    <p>© 2026 {t["foot_by"]}</p>
    <nav aria-label="Footer">
      <a href="support.html">{t["nav_support"]}</a>
      <a href="privacy.html">{t["nav_privacy"]}</a>
      <a href="mailto:{MAIL}">{t["foot_contact"]}</a>
    </nav>
  </div>
</footer>
</body>
</html>
'''

def home(lang):
    t = T[lang]; asset = "../assets/" if lang == "fr" else "assets/"
    out = head(t, lang, "index.html", t["title_home"], t["desc_home"], asset)
    out += header(t, lang, "index.html", asset, "./" if lang=="fr" else "./", "home")
    levels = "".join(f'<span class="{"on" if i==t["lv_on"] else ""}">{html.escape(x)}</span>' for i, x in enumerate(t["lv"]))
    video = f'''<div class="wrap video-slot" id="promo" hidden>
  <video controls preload="metadata" playsinline poster="{asset}promo-{lang}-poster.jpg" aria-label="{t["video_label"]}">
    <source src="{asset}promo-{lang}.mp4" type="video/mp4">
  </video>
</div>
<script>
(function(){{var s=document.getElementById("promo"),v=s&&s.querySelector("video");
if(!v)return;v.addEventListener("loadedmetadata",function(){{s.hidden=false}});
v.addEventListener("error",function(){{s.hidden=true}},true);v.load();}})();
</script>'''
    steps = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in t["steps"])
    proof = "".join(f"<div><h3>{a}</h3><p>{b.format(priv='privacy.html')}</p></div>" for a, b in t["proof"])
    feats = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in t["feats"])
    reqs = "".join(f"<li>{r}</li>" for r in t["reqs"])
    out += f'''<main id="main">
<div class="wrap hero">
  <div>
    <p class="eyebrow">{t["app_tagline"] if lang=="en" else "Dictée vers prompt, 100 % hors ligne"}</p>
    <h1>{t["h1"]}</h1>
    <p class="lede">{t["lede"]}</p>
    <div class="cta-row">
      <a class="btn" href="{STORE}">{APPLE}<span>{t["cta"]}</span></a>
      <p class="fine">{t["cta_note"]}</p>
    </div>
  </div>
  <div class="mock" role="img" aria-label="{html.escape(t["mock_said"])} → {html.escape(t["mock_out"].replace("<b>","").replace("</b>",""))}">
    <div class="mock-bar" aria-hidden="true"><i></i><i></i><i></i><span>{t["mock_title"]}</span></div>
    <div class="mock-body" aria-hidden="true">
      <div><p class="mock-label">{t["mock_said_l"]}</p><p class="mock-said">{t["mock_said"]}</p></div>
      <div><p class="mock-label">{t["mock_out_l"]}</p><div class="mock-out">{t["mock_out"]}</div></div>
      <div class="levels">{levels}</div>
    </div>
  </div>
</div>
{video}
<section class="wrap" id="how" aria-labelledby="how-h">
  <div class="sec-head"><p class="eyebrow">{t["how_eyebrow"]}</p><h2 id="how-h">{t["how_h"]}</h2></div>
  <ol class="steps">{steps}</ol>
</section>
<section class="band" id="privacy-first" aria-labelledby="priv-h">
  <div class="wrap">
    <p class="eyebrow">{t["priv_eyebrow"]}</p>
    <h2 id="priv-h">{t["priv_h"]}</h2>
    <p style="margin-top:var(--s4)">{t["priv_p"]}</p>
    <div class="proof">{proof}</div>
  </div>
</section>
<section class="wrap" id="features" aria-labelledby="feat-h">
  <div class="sec-head"><p class="eyebrow">{t["feat_eyebrow"]}</p><h2 id="feat-h">{t["feat_h"]}</h2></div>
  <dl class="features">{feats}</dl>
</section>
<section class="alt" id="requirements" aria-labelledby="req-h">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{t["req_eyebrow"]}</p><h2 id="req-h">{t["req_h"]}</h2></div>
    <ul class="reqs">{reqs}</ul>
    <div class="cta-row" style="margin-top:var(--s7)"><a class="btn" href="{STORE}">{APPLE}<span>{t["cta"]}</span></a></div>
  </div>
</section>
</main>
'''
    out += footer(t)
    return out

def privacy(lang):
    t = T[lang]; asset = "../assets/" if lang == "fr" else "assets/"
    out = head(t, lang, "privacy.html", t["title_priv"], t["desc_priv"], asset)
    out += header(t, lang, "privacy.html", asset, "./", "privacy")
    toc = "".join(f'<li><a href="#{i}">{html.escape(h)}</a></li>' for i, h, _ in t["p_secs"])
    body = "".join(f'<h2 id="{i}">{h}</h2>' + "".join(ps) for i, h, ps in t["p_secs"])
    out += f'''<main id="main" class="wrap doc">
  <h1>{t["p_h1"]}</h1>
  <p class="meta">{t["p_meta"]}</p>
  <div class="doc-grid">
    <nav class="toc" aria-label="{t["p_toc"]}"><ul>{toc}</ul></nav>
    <article>{body}</article>
  </div>
</main>
'''
    # first h2 should not have big top margin
    out = out.replace('<article><h2 id="summary">', '<article><h2 id="summary" style="margin-top:0">')
    out += footer(t)
    return out

def support(lang):
    t = T[lang]; asset = "../assets/" if lang == "fr" else "assets/"
    out = head(t, lang, "support.html", t["title_supp"], t["desc_supp"], asset)
    out += header(t, lang, "support.html", asset, "./", "support")
    faq = "".join(f"<details><summary>{q}</summary>{a.format(priv='privacy.html')}</details>" for q, a in t["faqs"])
    out += f'''<main id="main" class="wrap doc">
  <h1>{t["s_h1"]}</h1>
  <p class="lede">{t["s_lede"]}</p>
  <h2>{t["faq_h"]}</h2>
  <div class="faq">{faq}</div>
  <h2>{t["contact_h"]}</h2>
  <div class="contact-box">
    <p>{t["contact_p"]}</p>
    <p><a href="mailto:{MAIL}">{MAIL}</a></p>
    <p><a href="{ISSUES}" rel="noopener">{t["contact_issue"]}</a> <span class="fine">{t["contact_issue_note"]}</span></p>
  </div>
</main>
'''
    out += footer(t)
    return out

for lang in ("en", "fr"):
    d = ROOT if lang == "en" else os.path.join(ROOT, "fr")
    os.makedirs(d, exist_ok=True)
    for name, fn in (("index.html", home), ("privacy.html", privacy), ("support.html", support)):
        with open(os.path.join(d, name), "w", encoding="utf-8") as f:
            f.write(fn(lang))
print("ok")
