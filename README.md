# Mastermind en Python
Jeu du Mastermind développé en Python avec pygame, dans le cadre de la SAE S1.01 du BUT Informatique (IUT de Maubeuge).
L'ordinateur choisit une combinaison secrète de 5 couleurs, et le joueur doit la deviner en un nombre limité d'essais.
## Aperçu

<img width="799" height="704" alt="master" src="https://github.com/user-attachments/assets/06531a1e-9be2-4a97-98a7-616f1a56d13d" />

## Règles du jeu

- L'ordinateur génère un secret de 5 couleurs.
- À chaque tour, tu proposes une combinaison de 5 couleurs.
- Le jeu t'indique :
  - les couleurs **bien placées**
  - les couleurs **présentes mais mal placées**
- Tu gagnes si tu trouves le secret avant la fin des essais.

## Installation

Prérequis : Python 3 et pygame.
```
pip install pygame
```

Puis récupère le projet :
```
git clone https://github.com/[Kataline]/mastermind.git
cd mastermind
```

## Lancer le jeu
```
python [main.py]
```

## Structure du projet
| Fichier | Rôle |
|`demo.py` | Essai pour que j'apprenne le pygame
| `mm.py` | Bibliothèque du jeu (fonctions de base, dont la fonction `distance`) |
| `[main.py]` | Programme principal |
| `rapport/` | Rapport de mon avancement (pseudo-code, tableau des variables, tests) |

## Ce que j'ai appris
- Utiliser pygame pour afficher une interface simple
- Découper un programme en fonctions avec paramètres et valeurs retournées
- Tester son code et documenter son travail

## Kataline

BUT1 Informatique, IUT de Maubeuge
