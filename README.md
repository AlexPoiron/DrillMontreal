# DrillMontreal
Ton Drilleur préféré est bloqué à son hôtel et ne peut rejoindre son showcase à Montréal, aide-le en allumant la neige telle les opps.
En effet, la neige est plus que présente sur le réseau routier et bouche toute la circulation. 
Notre mission est la suivante, déneiger le plus efficacement Montréal afin de pouvoir assister à ce showcase de qualité.

Celle-ci se découpe en 2 parties :
* Faire une analyse de ce réseau routier montréalais suffisamment fine pour y retrouver des informations croustillantes.
* Déblayer toutes les routes le plus rapidement et efficacement possible.

## Installation des paquets

Pour la partie theorique du probleme, 

Pour la partie réelle et appliquée à cette magnifique ville qu'est Montréal, assurez vous d'avoir dans un premier temps les bibliothèques OSMnx, networkX, colorama et datetime d'installées dans un environnement virtuel sur votre ordinateur. 
* https://osmnx.readthedocs.io/en/stable/
* https://networkx.org/documentation/stable/index.html
* https://pypi.org/project/colorama/
* https://docs.python.org/3/library/datetime.html

## Exécution de la solution
 
*  **conda activate ox** pour vous mettre dans un environnement virtuel avec OSMnx
*  **bash script.sh** un script exécutant une démonstration de notre solution sur le quartier Outremont à Montréal. Les options d'affichage des cartes étant activées, il est nécessaire de fermer les fenêtres s'ouvrant pour continuer l'exécution de notre code.

## Notre travail détaillé

* Dans le dossier `real_case/` vous trouverez 2 fichiers jupyter qui décrivent pas à pas l'exécution de notre code pour la partie sur le drone et la partie sur les déneigeuses.
* Dans le dossier `theoretical_case/` vous trouverez un fichier jupyter expliquant notre solution d'un point de vue théorique.

## Descriptif de la structure

* **`real_case/`** : une sous-arborescence consacrée à l’étude du cas réel d'un quartier de Montréal, LaSalle
* **`theoretical_case/`** : une sous-arborescence consacrée à l’étude du cas théorique 
* **`AUTHORS`** : fichier contenant la liste des créateurs de cette solution
* **`LINKS`** : fichier contenant le lien vers la vidéo de présentation de la solution
* **`script.sh`** : le script exécutant une démonstration de notre solution appliquée sur le quartier Outremont à Montréal
