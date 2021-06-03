# DrillMontreal
Ton Drilleur préféré est bloqué à son hôtel et ne peut rejoindre son showcase à Montréal, aide-le en allumant la neige telle les opps.
En effet, la neige est plus que présente sur le réseau routier et bouche toute la circulation. 
Notre mission est la suivante, déneiger le plus efficacement Montréal afin de pouvoir assister à ce showcase plus que mouvementé de qualité.

Celle-ci se découpe en 2 parties :
* Faire une analyse de ce réseau routier montréalais suffisament fine pour y retrouver des informations croustillantes.
* Déblayer toutes les routes le plus rapidement et efficacement possible.

## Installation des paquets

Pour la partie theorique du probleme, 

Pour la partie réelle et appliquée à cette magnifique ville qu'est Montréal, assurez vous d'avoir dans un premier temps les bibliothèques OSMnx, networkX, colorama et datetime d'installées dans un environnement virtuel sur votre ordinateur. 
* https://osmnx.readthedocs.io/en/stable/
* https://networkx.org/documentation/stable/index.html
* https://pypi.org/project/colorama/
* https://docs.python.org/3/library/datetime.html

## Exécution de la solution :
 
*  **conda activate ox** pour vous mettre dans un environnement virtuel avec OSMnx
*  **./script.sh** un script exécutant une démonstration de notre solution sur la ville du Kremlin-Bicêtre. Les options d'affichage des cartes étant activées, il est nécessaire de fermer les fenêtres s'ouvrant pour continuer l'exécution de notre code.

## Descriptif de la structure

* **`real_case`** : une sous-arborescence consacrée à l’étude du cas réel d'un quartier de Montréal, LaSalle
* **`theoretical_case`** : une sous-arborescence consacrée à l’étude du cas théorique 
* **`AUTHORS`** : fichier contenant la liste des créateurs de cette solution
* **`LINKS`** : fichier contenant le lien vers la vidéo de présentation de la solution
* **`script.sh`** : le script exécutant une démonstration de notre solution appliquée à la ville du Kremlin-Bicêtre
* **`script_theoretical.sh`** : le script ouvrant le jupyter contenant le code dans le cas théorique pour le parcours de graphe eulérien non orienté
* **`script_real.sh`** : le script ouvrant le jupyter contenant les codes dans le cas réel pour le drone et pour les déneigeuses
