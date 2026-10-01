# Chiffrement de César & Cryptanalyse

Chiffrement d'un message avec César. Et le déchiffrer sans disposer de clé à l'aide de la méthode de bruteforce et d'analyse fréquentielle.

## Objectif du projet


Objectif :
Créer un programme Python capable de :
chiffrer un texte avec César, et réussir à le déchiffrer sans la clé. Afin d'améliorer mes compétences en cryptanalyse. Et aussi pour me familiariser avec la plateforme GitHub 

## Fonctionnalités

- Chiffrer un texte avec une clé donnée
- Déchiffrer un texte avec une clé connue
- Retrouver la clé par force brute (bruteforce)
- Retrouver la clé automatiquement par analyse fréquentielle
- Interface en ligne de commande (menu terminal)


## Structure du projet

- `cesar.py` : permet de chiffrer un texte avec une clé donnée. En utilisant la logique du chiffrement de césar.
- `cryptanalyse.py` : Permet le déchiffrement sans avoir accès à la clé. Premièrement par le bruteforce et enfin par l'analyse fréquentielle.
- `main.py` : menu terminal, contenant la liste des fonctionnalités permettant leur utilisation.


## Installation et utilisation

1. Cloner le dépôt :
  git clone https://github.com/M18-fred/cesar-cipher.git
2. Se placer dans le dossier du projet : 
  cd cesar-cipher
3. Lancer le programme :
  python main.py

Prérequis : Python 3.x (aucune bibliothèque externe nécessaire)


## Exemple d'utilisation


```
=== Chiffrement de César ===
1. Chiffrer un texte
2. Déchiffrer un texte
3. Bruteforce (essayer toutes les clés)
4. Deviner la clé (analyse fréquentielle)
5. Quitter

Veuillez choisir une option : 4
Entrer le texte chiffré : Hjhn jxy zs jcjwhnhj...
Clé devinée : 5
Texte clair : Ceci est un exercice...
```


## Comment fonctionne l'analyse fréquentielle ?


Généralement en langue française, la lettre 'E' est la plus utilisée dans les textes. Par conséquent, l'analyse fréquentielle consiste à identifier la lettre la plus utilisée après chiffrement et la considérer comme étant la lettre 'E' et enfin donner la clé en fonction de l'écart entre les deux (dans le code ASCII)


## Limites connues

- L'analyse fréquentielle peut se tromper sur un texte court. Exemple : "bonjour madame"
- Ce programme simule un scénario où le texte chiffré est déjà "intercepté"
  (pas de vraie interception réseau)


## Ce que j'ai appris


- Sur Python : ord()/chr() et le modulo pour gérer un alphabet circulaire, les dictionnaires pour compter des occurrences, les tuples et leur déballage, l'intérêt de séparer son code en plusieurs fichiers/modules (if __name__ == "__main__")

- Sur Git/GitHub : le cycle add → commit → push, l'importance d'un .gitignore, ce que fait réellement un renommage de fichier pour Git

- Sur la cryptographie/cryptanalyse en général : Malgré son chiffrement, César reste un chiffrement faible (seulement 26 clés possibles) et obsolète notre époque (dans le sens où il n'est plus utilisé pour sécuriser quoi que ce soit aujourd'hui). En outre, le principe de l'analyse fréquentielle dans un texte chiffré et selon un dictionnaire spécifique, la distinction entre "casser un chiffrement" et "intercepter des données" car dans notre cas, nous ne faisons aucune interception de données.


## Pistes d'amélioration


- Comparaison statistique complète des fréquences (pas juste la lettre la plus fréquente)
- Gérer d'autres langues
- Interface graphique au lieu du terminal
- Simuler une vraie interception réseau


## Technologies utilisées

- Python 3.x
