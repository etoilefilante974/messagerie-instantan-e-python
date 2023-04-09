#import int
#import meteo
#import voit
#import tk
import threading 
import tkinter as tk
from datetime import datetime

def fairejoli():
    for i in range(10):
        print(i*"x")
    print("bienvenue sur le code de Mathias")
    for i in range(10):
        print((10-i)*"x")


def ecriretfichier():
    with open('C:/Users/jauze/Desktop/voiture.txt','w') as filin:
        print("écrivez un texte dans le fichier")
        testetest=input("")
        filin.write(testetest)

def ihm():
    racine=tk.Tk()
    label=tk.Label(racine, text="Bienvenur sur l'IHM de Mathias")
    label1=tk.Label(racine, text=datetime.now().time())
    label2=tk.Label(racine, text=C)
    bouton=tk.Button(racine, text="fexit", command=racine.destroy)
    label.pack(pady=20)
    label1.pack()
    label2.pack()
    bouton.pack(pady=20)
    racine.geometry("500x500")
    #racine.mainloop()
    pass


def afficher():
    print("je suis la fonction main")
if __name__=="__main__":
    print("rentrez le texte")
    C=input()
    fairejoli()
    g=threading.Thread(target=ihm())
    g.start()
    ecriretfichier()
    print("mai,,,,")
    nom="alain"
    print(f"mon nom est  {nom}")
    print("mon nom est ", nom,"de")
    afficher()

    
import socket

    
