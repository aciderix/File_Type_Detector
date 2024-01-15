import os
import magic
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def retrouver_extensions(dossier, progressbar):
    total_fichiers = len([f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))])
    with open("liste_fichiers.txt", "w") as fichier_sortie:
        mime = magic.Magic()
        for i, fichier in enumerate(os.listdir(dossier)):
            chemin_complet = os.path.join(dossier, fichier)
            if os.path.isfile(chemin_complet):
                fichier_sortie.write(f"{fichier}: {mime.from_file(chemin_complet)}\n")
            
            # Mettre à jour la barre de progression
            progression = int((i + 1) / total_fichiers * 100)
            progressbar["value"] = progression
            fenetre.update_idletasks()

    return "Processus terminé. Vérifiez le fichier liste_fichiers.txt."

def parcourir_dossier():
    dossier = filedialog.askdirectory()
    if dossier:
        barre_progression.start()
        resultat = retrouver_extensions(dossier, barre_progression)
        barre_progression.stop()
        label_resultat.config(text=resultat)
        bouton_ouvrir.config(state=tk.NORMAL)

def ouvrir_fichier():
    os.system("liste_fichiers.txt")

# Création de l'interface graphique
fenetre = tk.Tk()
fenetre.title("Détecteur d'Extensions")

# Bouton pour parcourir le dossier
bouton_parcourir = tk.Button(fenetre, text="Parcourir le dossier", command=parcourir_dossier)
bouton_parcourir.pack(pady=20)

# Barre de progression
barre_progression = ttk.Progressbar(fenetre, orient="horizontal", length=300, mode="determinate")
barre_progression.pack()

# Label pour afficher le résultat
label_resultat = tk.Label(fenetre, text="")
label_resultat.pack()

# Bouton pour ouvrir le fichier texte généré
bouton_ouvrir = tk.Button(fenetre, text="Ouvrir le fichier texte", command=ouvrir_fichier, state=tk.DISABLED)
bouton_ouvrir.pack(pady=20)

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
