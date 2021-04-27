import pypokedex
from tkinter import *

# pokemon = pypokedex.get(name='pikachu')
# print(pokemon.sprites[0]["default"])
# print(pokemon)

def pokemon(value):
   p = pypokedex.get(name=value)
   print(p)

def getValueInput():
   value = name_pokemon.get()
   return value

#Inite module
screen = Tk()
#window
screen.title('Pokemon Guide')
screen.geometry('300x300+800+350')

#ENTRY DATA
name_pokemon = Entry(screen, bd=1)
name_pokemon.place(x=90, y=150)

#Button
btn = Button(screen, text='Search', command=lambda: pokemon(getValueInput()))
btn.pack()
btn.place(x=125, y=250)


screen.mainloop()

