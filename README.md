# L'IA & toi

Atelier interactif pour les lycéens, notamment en voie professionnelle :
45 minutes, huit actes, ouverture et bilan compris. Auteur : Eneric (NricL).

- Atelier : https://nricl.github.io/LyceeIA/
- Guide animateur : https://nricl.github.io/LyceeIA/?guide=animateur
- Fiche lycéen : https://nricl.github.io/LyceeIA/?guide=eleve

Le bouton **Guides** ouvre les ressources sans quitter la séance. Le guide
animateur contient objectifs, minutage, consignes, relances, réponses attendues,
vigilances et variantes sans connexion. La fiche lycéen propose des repères,
trois prompts copiables et un mini-défi. Chaque ressource peut être imprimée ou
enregistrée en PDF depuis le navigateur. Les notes animateur contiennent les
réponses : les garder sur papier ou sur un écran non projeté.

## Utilisation

Ouvrir `index.html` dans un navigateur récent (Edge, Chrome, Firefox ou Safari).
Tout est intégré : illustrations, logo Microsoft, styles, scripts et guides.
Aucun serveur, compte, modèle d'IA ou réseau n'est nécessaire. Les liens vers
Microsoft, la CNIL et le CLEMI sont des compléments en ligne.

Les flèches naviguent entre les actes ; les boutons et cartes sont accessibles
au clavier. Le minuteur démarre manuellement et se met en pause dans les guides.
Les interactions restent en mémoire uniquement et sont réinitialisées au
rechargement. La copie des prompts dépend des autorisations du navigateur :
en cas de refus, le texte est sélectionné pour une copie manuelle.

Les probabilités de génération et les résultats du duel de prompts sont des
simulations préparées. Les textes du quiz sont fictifs, sans provenance
authentifiée ; leur style n'est pas une preuve d'origine. Les situations
éthiques et métiers sont des illustrations, pas des performances garanties.
L'atelier ne collecte aucune donnée d'élève. Toute démonstration externe reste
facultative et soumise aux règles de l'établissement et aux conditions d'âge.

## Publication et export autonome

GitHub Pages publie `index.html` depuis la racine de `main`. Le même fichier
peut être transmis tel quel et ouvert hors connexion.

Après une modification, intégrer le logo et vérifier l'absence de ressources
externes avec Python (bibliothèque standard, aucune installation nécessaire) :

```powershell
python .\package_site.py
python .\package_site.py --export ..\lycee-ia-atelier-autonome.html
```

L'export refuse d'écraser un fichier existant : choisir un autre nom si besoin.
Le logo officiel embarqué provient de
https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png ; il n'est pas redessiné.
Les guides suivent le thème clair/sombre du système, sans modifier l'identité
visuelle sombre de la présentation.
