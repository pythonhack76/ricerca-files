#un programma per cercare files in directory 
from tkinter import *
import tkinter as tk
import os 

def esegui_ricerca():
    pass

def reset_ricerca():
    pass

def view_ricerca():
    view = ricerca.get()
    print(view)
    



#creo la finestra per applicativo
window = Tk()
window.geometry("500x500")
window.title("ricerca il tuo file")
window.resizable(False, False)
window.configure(background="lightblue")
my_font=('times', 8, 'bold')

#creo titolo
label0 = Label(text = "Cerca e trova Files")
label0.place(x = 180, y = 20)
#creo campo per ricerca file
label= Label(text = "Inserisci indirizzo cartella:")
label.place(x = 30, y = 40)
label.config(bg='lightgreen', padx=10)

ricerca = Entry(text = "")
ricerca.place(x=190, y=40, width=200, height=20)

risultato = Label(font="calibri", height="35", width="70")

#inserisco bottone per avvio ricerca
button = Button(text = "ricerca", command = view_ricerca)
button.place(x=200, y=80, width=75, height=35)

button = Button(text = "chiudi", command = window.destroy)
button.place(x=290, y=80, width=75, height=35)





#start per il programma 
window.mainloop() 