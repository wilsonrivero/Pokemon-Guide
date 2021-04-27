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
label_input = Label(screen, text='Id or Name', font=('Arial', 18))
label_input.place(x=85, y=100)
name_pokemon = Entry(screen, width=70, bd=1)
name_pokemon.place(x=0, y=150)

#Button
btn = Button(screen, text='Load Pokemon',command=lambda: pokemon(getValueInput()))
btn.pack()
btn.place(x=100, y=220)


screen.mainloop()

