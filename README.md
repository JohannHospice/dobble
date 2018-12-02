# Dobble

Le jeu Dobble utilise des cartes dont chacune représente k=8 dessins choisis parmi n=57 dessins différents; chaque dessin apparaît sur au plus l=8 cartes, et chaque paire de cartes possède exactement d=1 dessin en commun.

Le but du devoir est de construire de tels jeux de cartes, les plus gros possible, pour d'autres 4-uplets (n, k, l, d).

### En entrée : 

4 entiers n, k, l, d lus sur la ligne de commande

### En sortie : 

la taille du plus gros jeu de cartes possible utilisant n symboles, avec k symboles par carte, chaque symbole apparaissant au plus l fois, et tel que deux cartes quelconques partagent exactement d symboles.

L'affichage doit produire exactement 3 lignes, chacune éventuellement vide :

- la __taille maximale__ d'un tel jeu de cartes,
- le __nombre de solutions__ distinctes,
- la description d'__une solution__, sous la forme d'une __suite de mots__ sur l'alphabet {0,1}, __séparés par des espaces__; par exemple, le mot ```00110``` code une carte représentant les 3ème et 4ème symboles d'un ensemble de 5 symboles, et une solution du problème pour n=5, k=2, l=4 et d=1 est : ```00011 00110 01010 10010```.
Si vous ne faites pas une partie, laisser la ligne vide.

Par exemple, la seule sortie possible pour n=4, k=l=3 et d=2  est : 
```
4
1
0111 1011 1101 1110
```
Un exemple plus gros : une sortie possible pour n=7, k=l=4 et d=2  est : 
```
7
30
0001111 0110011 1010101 1101001 1100110 1011010 0111100
```
##### Contributeurs: Johann Hospice et Andy Limmois
