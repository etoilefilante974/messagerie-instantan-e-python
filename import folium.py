import folium
import webbrowser




from tkinter import *
import tkinter as tk
#fenetre=Tk()
#print("t")
#message = tk.Label(fenetre, text="Bonjour le monde")
#message.pack()

#import int
#import meteo
#import voit
#import tkl
import sys
print(sys.path)
import threading 
import tkinter as tk
from tkinter import *
from datetime import datetime


#import msnp

res=""
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

def sq(res):
    import sqlite3
    connection = sqlite3.connect("C:/Users/jauze/Desktop/dbz.db")
    i=2
    i+=1
    cursor=connection.cursor()
    fg=(cursor.lastrowid,res,i)
    cursor.execute('INSERT INTO t_nb VALUES(?,?,?)',fg)
    connection.commit()

def Lire():
    import sqlite

def carte():
    webbrowser.open("file://C:/Users/jauze/Desktop/essa.html")


class affichage():
    
    def __init__(self):
        def getEntry():
            res = chef.get()
            print("ceci est le texte tape", res)
            sq(res)
            s,q=res.split()
            s=int(s)
            q=int(q)
            #print("ceci est le debut",s, "et cice",q)
            m = folium.Map(location=[s, q])
            m.save('essa.html')
        racine=tk.Tk()
        label=tk.Label(racine, text="Bienvenur sur l'IHM de Mathias")
        label1=tk.Label(racine, text=datetime.now().time())
        label2=tk.Label(racine, text=C)
        label3=tk.Label(racine, text=D)
        bouton=tk.Button(racine, text="fexit", command=racine.destroy)
        chef = tk.Entry(racine,bg="white")
        bouton1=tk.Button(racine, text="Envoi texte sur base de donnée", command=getEntry)
        bouton2=tk.Button(racine, text="Lire Base de donné", command=Lire)
        bouton3=tk.Button(racine, text="afficher carte", command=carte)
        label.pack(pady=20)
        label1.pack()
        label2.pack()
        label3.pack()
        chef.pack()
        bouton1.pack()
        bouton.pack(pady=20)
        bouton2.pack()
        bouton3.pack()
        racine.geometry("500x500")
        racine.mainloop()
    

def ihm():      
    racine=tk.Tk()
    label=tk.Label(racine, text="Bienvenur sur l'IHM de Mathias")
    label1=tk.Label(racine, text=datetime.now().time())
    label2=tk.Label(racine, text=C)
    bouton=tk.Button(racine, text="fexit", command=racine.destroy)
    
    chef = tk.Entry(racine,bg="white")
    #bouton1=tk.Button(racine, text="change couleur", command=print(label2.get()))
    label.pack(pady=20)
    label1.pack()
    label2.pack()
    chef.pack()
    #bouton1.pack()
    bouton.pack(pady=20)
    racine.geometry("500x500")
    #racine.mainloop()
    pass


def afficher():
    print("je suis la fonction main")
if __name__=="__main__":
    #msn=msnp.Session()
    print("rentrez le texte")
    res=""
    C=input()
    D="---"
    fairejoli()
    #g=threading.Thread(target=affichage())
    #g.start()
    app=affichage()
    ecriretfichier()
    print("mai,,,,")
    nom="alain"
    print(f"mon nom est  {nom}")
    print("mon nom est ", nom,"de")
    afficher()

    
import socket

    





