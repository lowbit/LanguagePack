# AnySoftKeyboardLanguagePackFrench
## English
French language pack for the AnySoftKeyboard software.

### State of features
- Experimental: may change any time, and even be removed. Don't rely on it.
- Release candidate: available for testing. If no bugs are discovered, it goes directly in stable state.
- Stable: General Availability. It should only change for 3rd party updates or discovered bugs.

By default, features are in experimental state.

### Dictionaries
This pack includes three dictionaries:
- English-French: it is a mix of the English dictionary included in AnySoftKeyboard (based on AOSP) and the French AOSP dictionary (see known bugs below). It is a large dictionary. ~300 000 words.
- French AOSP: it is based on the AOSP French dictionary, with the original mistakes (the o and e ligature is written oe instead of œ). WIP: words with accents are never shown in suggestions. ~150 000 words.
- [Release candidate] French Dicollecte: it is based on the Dicollecte French dictionary, under MPLv2 license. Only the most frequent words are included. It is a slightly bigger dictionnary. ~250 000 words.

Auto correct in French dictionaries is based on LibreOffice work, under LPGLv3+ license. Doesn’t work.
WIP for the English-French dictionary.

### Keyboards
A specific bottom row has been designed for use with French keyboards, it is strongly recommended to use it with the keyboards included in this pack.

This pack includes four keyboards mainly used in French-speaking countries:
- AZERTY as arranged in France and Belgium (the two variants are included)
- QWERTY inspired of the Multilingual Canadian keyboard (CAN/CSA Z243.200-92 norm)
- QWERTZ as arranged in Switzerland
- Ergonomic and French bépo

You can find three variants of each keyboard:
- Classic keyboard: 26 keys on 3 rows (maximum of 10 keys per row).
- With accents keyboard: up to 31 keys on 3 rows (maximum of 11 keys per row), with dedicated keys for accents. On AZERTY keyboard, there is still a maximum of 10 keys per row, but a 4th row has been added.
- Full keyboard: it is a 60% keyboard, as found on most PC. May be useful on big screens or in landscape.

All keyboards include symbols on long press.
(WIP) As far as possible, all keyboards are designed to give a quick access to the most common characters used in French language on long press, while matching the original layout at most.

## Français
Pack de langue pour le français pour le logiciel AnySoftKeyboard.

### État des fonctionnalités
- Expérimental : peut changer à tout moment, et même être supprimé. Ne comptez pas dessus.
- Admissible : disponible pour les tests. Si aucun bogue n’est découvert, la fonctionnalité passe directement en état stable.
- Stable : disponibilité générale. Ne devrait changer que pour les mises à jour tierces ou bogues découverts.
Par défaut, les fonctionnalités sont expérimentales.

### Dictionnaires
Ce pack inclue trois dictionnaires :
- Anglais-Français : un mélange du dictionnaire anglais d’AnySoftKeyboard (basé sur AOSP) et du dictionnaire français d’AOSP (voir bogues connus ci-dessous). ~300 000 mots.
- Français d’AOSP : basé sur le dictionnaire français d’AOSP, avec ses fautes originales (la ligature entre le o et le e est écrite oe au lieu de œ). Bogue : les mots avec accents ne sont jamais proposés dans les suggestions. ~150 000 mots.
- [Admissible] Français de Dicollecte : basé sur le dictionnaire français de Dicollecte, sous licence MPLv2. Seuls les mots les plus fréquents ont été inclus. ~250 000 mots.

L’auto correction dans les dictionnaires français est basé sur le travail de LibreOffice, sous licence LPGLv3+. Ne fonctionne pas.
Non disponible pour le dictionnaire Anglais-Français.

### Claviers
Une rangée du bas spécifique a été conçue pour utilisation avec les claviers français, il est fortement recommandé de l’utiliser avec les claviers inclus dans ce pack.

Ce pack inclue quatre claviers principalement utilisés dans les pays francophones :
- AZERTY tel que disposé en France et en Belgique (les deux variantes sont incluses)
- QWERTY inspiré du clavier multilingue canadien (norme CAN/CSA Z243.200-92)
- QWERTZ tel que disposé en Suisse
- Bépo francophone et ergonomique

Vous trouverez trois variantes de chaque clavier :
- Clavier classique : 26 touches sur 3 rangées (maximum de 10 touches par rangée). Si la disposition le permet, une touche dédiée à l’apostrophe fait office de 28e touche.
- Clavier avec accents : jusqu’à 31 touches sur 3 rangées (maximum de 11 touches par rangée), avec touches dédiées pour les accents. Sur le clavier AZERTY, il y a toujours un maximum de 10 touches par rangée, mais une 4e rangée a été ajoutée.
- Clavier complet : clavier 60 %, tel qu’on le trouve sur la plupart des PC. Peut être utile sur des grands écrans ou en mode paysage.

Tous les claviers incluent les symboles sur appui long.
(en cours) Autant que possible, tous les claviers sont conçus de façon à donner un accès rapide aux caractères les plus utilisés du français sur appui long, tout en conservant la disposition originale au maximum.

## Technical
Keyboards designed obey these rules (specs can change, still experimental state):
- Quick access to all French letters: A a À à Â â Ä ä Ã ã Æ æ B b C c Ç ç D d E e É é È è Ê ê Ë ë F f G g H h I i Ì ì Î î Ï ï J j K k L l M m N n Ñ ñ O o Ò ò Ô ô Ö ö Õ õ Œ œ P p Q q R r S s T t U u Ù ù Û û Ü ü V v W w X x Y y Ÿ ÿ Z z
- Access to common typographic symbols: _ - ' . , ; : ! ? @ & § ~ ^ ` ¨ ° | ( ) { } [ ] / \ < > " # « » … – — ’
- Access to numbers and mathematicals symbols: 0 1 2 3 4 5 6 7 8 9 ² ³ * + = % µ
- Access to currency symbols: € $ £
- Access to latin letters from official languages of European countries: Ă ă Ā ā Å å Ą ą Ć ć Ċ ċ Č č Ď ď Đ đ Ė ė Ě ě Ē ē Ę ę Ġ ġ Ģ ģ Ħ ħ Ī ī Į į Ĳ ĳ Ķ ķ Ļ ļ Ł ł Ń ń Ň ň Ņ ņ Ő ő Ø ø Ŕ ŕ Ř ř Ś ś Š š Ș ș Ț ț Ť ť Ū ū Ů ů Ų ų Ű ű Ź ź Ż ż Ž ž ẞ ß
- Access to additional typographic symbols: “ ” ‘ „ ¡ ¿
- Access to additional languages characters:
    - asturien : ḷḷ ḥ
    - gallois : ŵ ŷ Ŵ Ŷ
    - turc & azéri : ğ Ğ ı İ Ə ə
    - islandais : ð Ð þ Þ
    - espéranto : ĉ ĝ ĥ ĵ ŝ ŭ Ĉ Ĝ Ĥ Ĵ Ŝ Ŭ
- Access to latin letters used in other languages from countries where there are a lot of French speakers:
    - wolof (Senegal): à À ó Ó ë Ë ñ Ñ ŋ Ŋ
    - peul (pulaar) (Senegal, Cameroun): ɓ Ɓ ɗ Ɗ ƙ Ƙ ƥ Ƥ ƭ Ƭ ƈ Ƈ ƴ Ƴ
- (Optional) Access to some of the greek alphabet letters (still need to decide): Α Β Δ Ε Φ Γ Η Ι Θ Κ Λ Μ Ν Ο Π Χ Ρ Σ Τ Υ Ω Ξ Ψ Ζ α β δ ε φ γ η ι θ κ λ μ ν ο π χ ρ σ τ υ ω ξ ψ ζ
- To have consistent keyboards, unless they have a dedicated key (mostly on 60% keyboards), some characters must be placed on strategic places on popup (rows are counted from bottom to top):
    - The 0 to 9 numbers must be accessed (and hinted) on the letters 1st to 10th of the last row
    - The ² must be accessed on the 2nd letter of the last row
    - The ³ must be accessed on the 3rd letter of the last row
    - The @ character must be directly accessed (and hinted) on the 1st letter of the 2nd row
    - The # character must be directly accessed (and hinted) on the 2nd letter of the 2nd row
    - The 3rd letter of the 2nd row must hint to your currency. For example, France and Belgium will use €, while Canadian will use $. On popup, show other currencies.
    - The * character must be directly accessed (and hinted) on the 4th letter of the 2nd row
    - The - character must be directly accessed (and hinted) on the 5th letter of the 2nd row
    - The _ character must be accessed on the key - or on the hinted key -.
    - The + character must be directly accessed (and hinted) on the 6th letter of the 2nd row
    - The = character must be directly accessed (and hinted) on the 7th letter of the 2nd row
    - The ( character must be directly accessed (and hinted) on the 8th letter of the 2nd row
    - The ) character must be directly accessed (and hinted) on the 9th letter of the 2nd row
    - The / character must be directly accessed (and hinted) on the 10th letter of the 2nd row. If the 10th letter doesn't exist, put it on the last letter of the 1st row.
    - The \ and | characters must be accessed on the 10th letter of the 2nd row. If the 10th letter doesn't exist, put it on the last letter of the 1st row.
    - The characters « » " : ! ? must be directly accessed (and hinted) on the letters of the middle of the 1st row. The exact place will depend on the number of characters of this line.
    - The character < must be accessed on the key « or on the hinted key «.
    - The character > must be accessed on the key » or on the hinted key ».
    - The characters “ and ” must be accessed on the key " or on the hinted key ".
    - The character ; must be accessed on the key : or on the hinted key :.
    - The character ¡ must be accessed on the key ! or on the hinted key !.
    - The character ¿ must be accessed on the key ? or on the hinted key ?.

Keyboards can also include additional letters to match their layout.

If you need latin letters from another language spoken in your country (particularly from African countries), open an issue to ask for them to be added.
Si vous avez besoin de lettres latines d’une autre langue parlée dans votre pays (en particulier pays d’Afrique), ouvrez un ticket pour demander à les ajouter.

See also: https://bepo.fr/wiki/Caract%C3%A8res_pris_en_charge
