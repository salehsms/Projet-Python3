*** Monôme ***
*** SALEH MAHAMAT SALEH ***

# Projet - Jeu de la Vie (ALGO3 - python)

Ce projet implémente le **Jeu de la Vie de Conway** en python , dans le cadre du cours `ALGO3.`

Il comprend deux parties :

- **Partie 1** : version console
- **Partie 2** : interface graphique avec Tkinter

---

## Règles du jeu 

Chaque cellule de la grille peut être **vivante (1)** ou **morte (0)**.

Pour chaque génération :

1. Une cellule vivante avec **2 ou 3** voisines  vivantes survit.
2. Une cellule morte avec **exactement 3** voisines vivantes devient vivante.
3. Sinon, la cellule meurt ou reste morte.

---
## Partie 1 - Mode Console

Fonctionnalités :
- Saisie du nombre de lignes et colones 
- Placement aléatoire de cellules vivantes
- Affichage génération par génération 
- Arrêt lorsque la grille devient vide 

Execution :

```bash
python3 jeudelavie.py

```

## Partie 2
La deuxieme partie propose une interface intuive permettant de manipuler la grille à la souris.

*** Fonctionnalités de l'interface ***

Création d'une grille personnalisée 
- choix du nombre de lignes **(1->50)**
- choix du nombre de colonnes **(1->50)**

Activation /Désactivation de cellles
- un clic sur une case inverse son état (vivante <-> morte)
Lancer la simulation **(start)**
Arrêter la similation **(Stop)**
Effacer la grille **(Clear)**


Générer une configuration aléatoire
- remplit environ 33% de la grille avec des cellules vivantes 

Animation automatique 
- passage d'une génération toutes les `1000 ms  ou 1 seconde`
- compter de génération afiché

Détection automatique
- grille vide -> arrêt + message 
- structure stable (aucune évolution ) -> arrêt + message

Aperçu du fonctionnement 
- la grille est dessinée dans un Canvas.
- les cellules vivantes sont affichées en `noir`, les mortes en `blanc.` 

- Chaque nouvelle génération est redessinée automatiquement.

```bash

python3 JeuDeLavie.py 

```