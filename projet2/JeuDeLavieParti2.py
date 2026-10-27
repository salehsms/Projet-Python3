import tkinter as tk
from tkinter import messagebox
import random

class JeuDeLaVie:
    def __init__(self, lignes , colonnes):

        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[0 for _ in range(colonnes)] for _ in range(lignes)]
        self.grille_precedent = None

    """
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
"""
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
                    if self.grille[voisin_ligne][voisin_colonne] == 1:
                        count += 1
        return count
    

    def etape_suivante(self):
        
        self.grille_precedent = [ligne[:] for ligne in self.grille]
        nouvelle_grille = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]


        for i in range(self.lignes):
            
            for j in range(self.colonnes):
                voisines = self.get_adjacents(i,j)


                if self.grille[i][j] == 1:
                    if  voisines in (2,3):
                        nouvelle_grille[i][j] = 1

                # Cellule vivante avec 2 ou 3 voisines -> reste vivante

                else: 
                    if voisines ==3:
                        nouvelle_grille[i][j] = 1
        self.grille =nouvelle_grille



    """
    def placer_cellules_aleatoirement(self , nombre):
        placees = 0

        while placees < nombre:
            i = random.randint(0 , self.lignes -1)
            j = random.randint(0, self.colonnes -1)

            if self.grille[i][j] == '-':
                self.grille[i][j] = '*'
                placees += 1
    """
    def est_structure_stable(self):
        return self.grille_precedent == self.grille

        
    def est_grille_vide(self):
        for ligne in self.grille :
            if 1  in ligne:
                return False
        return True
    
    def reinitialiser(self):
        self.grille = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]
        self.grille_precedent= None
    
class InterfaceGraphique:
    def __init__(self,root):
        
        self.root = root
        self.root.title("Jeu de la Vie")

        self.jeu = None
        self.simulation_active = False
        self.taille_celulle = 20

        self.generation = 0
        self.timer_id = None
        self.creer_interface()
    
    # Créer l'interface
    def creer_interface(self):
        config_frame = tk.Frame(self.root)
        config_frame.pack(pady= 10)

        tk.Label(config_frame , text="Lignes :").grid(row=0, column=0)
        self.entry_lignes = tk.Entry(config_frame , width=5)
        self.entry_lignes.insert(0, "20")
        self.entry_lignes.grid(row=0,column=1)

        tk.Label(config_frame , text="Colonnes :").grid(row=0,column=2)
        self.entry_colonnes = tk.Entry(config_frame , width=5)
        self.entry_colonnes.insert(0, "20")
        self.entry_colonnes.grid(row=0,column=3)

        tk.Button(config_frame , text="Créer Grille", command=self.creer_grille).grid(row=0 , column=4, padx=10)

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady= 10)

        self.btn_start = tk.Button(control_frame, text="Start" , command=self.demarrer , bg="green" , fg="white" , width=10)
        self.btn_start.grid(row=0, column=0 , padx= 5)

        self.btn_stop = tk.Button(control_frame , text="Stop" , command=self.arreter , bg="red" , fg="white", width=10)
        self.btn_stop.grid(row=0,column=1 , padx=5)

        self.btn_clear = tk.Button(control_frame , text="Clear",command=self.reinitialiser , bg="orange" , fg="white", width=10)
        self.btn_clear.grid(row=0 , column=2, padx=5)

        tk.Button(control_frame , text="Aléatoire" , command=self.remplir_aleatoire, width=10).grid(row=0,column=3, padx=5)

        self.label_generation = tk.Label(self.root, text="Génération : 0", font=("Arial" , 12, "bold"))
        self.label_generation.pack()

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(pady=10)

    # Fonction qui cree lle plateau
    def creer_grille(self):
        try:
            lignes = int(self.entry_lignes.get())
            colonnes = int(self.entry_colonnes.get())

            if  not (1 <= lignes <=50 and 1 <= colonnes <=50):
                messagebox.showerror("Erreur", "Valeurs entre 1 et 50")
                return 
            
            self.jeu = JeuDeLaVie(lignes, colonnes)
            self.generation =0
            self.label_generation.config(text="Génération : 0")

            largeur = colonnes*self.taille_celulle
            hauteur = lignes*self.taille_celulle

            self.canvas.config(width=largeur , height=hauteur)
            self.canvas.bind("<Button-1>" , self.clic_cellule)
            self.dessiner_grille()

        except ValueError:
            messagebox.showerror("Erreur",  "Entrez un nombre valide")


    def dessiner_grille(self):
        if not self.jeu:
            return
        
        self.canvas.delete("all")

        for i in range(self.jeu.lignes):
            for j in range(self.jeu.colonnes):
               
                x1 = j*self.taille_celulle
                y1 = i*self.taille_celulle

                x2 = x1 + self.taille_celulle
                y2 = y1 + self.taille_celulle

                couleur = "black" if self.jeu.grille[i][j] == 1 else "white"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur , outline="gray")

    def clic_cellule(self , event):
        if not self.jeu or self.simulation_active:
            return
        
        col = event.x // self.taille_celulle
        lig = event.y // self.taille_celulle

        if 0 <= lig < self.jeu.lignes and 0 <= col < self.jeu.colonnes:
            self.jeu.grille[lig][col]^=1
            self.dessiner_grille()

    
    def demarrer(self):
        if not self.jeu:
            messagebox.showwarning("Attention", "Créez une grille d'abord.")
            return 
        self.simulation_active = True
        self.executer_generation()

    def arreter(self):
        self.simulation_active = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def executer_generation(self):
        if not self.simulation_active:
            return 
        
        if self.jeu.est_grille_vide():
            self.arreter()
            messagebox.showinfo("Fin", "La grille est vide avant de commencer touchez sur Aléatoire.")

            return
        
        self.jeu.etape_suivante()
        self.generation += 1
        self.label_generation.config(text=f"Génération : {self.generation}")
        self.dessiner_grille()

        if self.jeu.est_structure_stable():
            self.arreter()

            messagebox.showinfo("Structure stable", f"Structure stable détectée à la génération {self.generation}.")
            return 
        self.timer_id = self.root.after(1000, self.executer_generation)

    def reinitialiser(self):
        self.arreter()
        if self.jeu :
            self.jeu.reinitialiser()
        self.generation = 0
        self.label_generation.config(text="Génération : 0")

        self.dessiner_grille()

    def remplir_aleatoire(self):
        if not self.jeu:
            messagebox.showwarning("Attention", "Créez une grille d'abord.")
            return 
        
        self.arreter()
        self.jeu.reinitialiser()
        

        total = self.jeu.lignes*self.jeu.colonnes
        nb = total// 3
        places = 0

        while places < nb:
            i = random.randint(0 , self.jeu.lignes - 1)
            j = random.randint(0, self.jeu.colonnes -1)

            if self.jeu.grille[i][j] == 0:
                self.jeu.grille[i][j] = 1
                places += 1

        self.generation = 0
        self.label_generation.config(text="Génération : 0")


if __name__== "__main__":
    root = tk.Tk()
    app = InterfaceGraphique(root)

    root.mainloop()


        
