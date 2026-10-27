
import random

class JeuDeLaVie:
    def __init__(self, lignes , colonnes):

        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [['-' for _ in range(colonnes)] for _ in range(lignes)]

    def afficher_grille(self):
        # En-tête colonnes 
        print("Colonne")
        print("        ", end="")
        for col in range(self.colonnes):
            print(col, end=" ")
        print()

        # Lignes

        for i in range(self.lignes):
            print(f"Ligne {i}", end=" ")
            for j in range(self.colonnes):
                print(self.grille[i][j], end=" ")
            print()

    def get_adjacents(self, ligne , colonne):
        """Conmter"""
        count = 0 
        for i in range(-1,2):
            for j in range(-1,2):
                if i== 0 and j== 0:
                    continue
                voisin_ligne = ligne + i
                voisin_colonne = colonne +j

                if(0 <= voisin_ligne < self.lignes and 
                   0 <= voisin_colonne < self.colonnes):
                    if self.grille[voisin_ligne][voisin_colonne] == '*':
                        count += 1
        return count
    

    def etape_suivante(self):
    
        nouvelle_grille = [['-' for _ in range(self.colonnes)] for _ in range(self.lignes)]


        for i in range(self.lignes):
            
            for j in range(self.colonnes):
                voisines = self.get_adjacents(i,j)

                # Cellule morte avec 3 voisines -> devient vivante

                if self.grille[i][j] == 0 and voisines == 3:
                    nouvelle_grille[i][j] = 1

                # Cellule vivante avec 2 ou 3 voisines -> reste vivante

                elif self.grille[i][j] == '*' and voisines in [2,3]:
                    nouvelle_grille[i][j] = '*'
        self.grille =nouvelle_grille



    
    def placer_cellules_aleatoirement(self , nombre):
        placees = 0

        while placees < nombre:
            i = random.randint(0 , self.lignes -1)
            j = random.randint(0, self.colonnes -1)

            if self.grille[i][j] == '-':
                self.grille[i][j] = '*'
                placees += 1
    

        
    def est_grille_vide(self):
        for ligne in self.grille :
            if '*' in ligne:
                return False
        return True
    
def main():
    """Fonction principale du programme"""
    print("="*50)
    print("       JEU DE LA VIE - GAME OF LIFE")
    print("="*50)


    # Demander la taille de la grille

    lignes = int(input("\nEntre le nombre de lignes: "))
    colonnes= int(input("\nEtrez le nombre de colonnes: "))

    jeu =JeuDeLaVie(lignes ,colonnes)

    max_cellules = lignes*colonnes

    nombre_cellules = int(input(f"Entrez le nombre de cellules vivantes (max {max_cellules}) : "))

    # verifier l'entrée
    if nombre_cellules > max_cellules:
        print(f"Attention : nombre limité à {max_cellules}")
        nombre_cellules =max_cellules
    # Placer les celulles aléatoirement
    jeu.placer_cellules_aleatoirement(nombre_cellules)
    
    # Afficher la génération initiale

    print("\n--- GÉNÉRATION 0 (Initial) ---")
    jeu.afficher_grille()
    
    # Boucle Principale

    generation = 1

    while True:
        #Demander si l'utilisateur veut continuer
        choix = input("Voulez-vous voir la prochaine génération ? (Y/N) :").upper()

        if choix != 'Y':
            print("\nFin du jeu. Au revoir !")
            break
        # verifions si la grille est vide
        if jeu.est_grille_vide():
            print("\nLa grille est vide. Fin du jeu.")
            break

        # Générer et affichons la prochaine génération 
        jeu.etape_suivante()
        print(f"\n--- GÉNÉRATION {generation} ---")
        jeu.afficher_grille()
        generation += 1
if __name__ == "__main__":
    main()

        

            
