import pypokedex
from tkinter import *

# pokemon = pypokedex.get(name='pikachu')
# print(pokemon.sprites[0]["default"])
# print(pokemon)

def main():
   #Inite module
   screen = Tk()
   #window
   screen.title('Pokemon Guide')
   screen.geometry('300x300+800+350')

   #Button
   btn = Button(screen, text='Search')
   btn.place(x=125, y=250)



   screen.mainloop()


main()