import pypokedex
from tkinter import *
import PIL.Image, PIL.ImageTk
import urllib3
from io import BytesIO

def LoadPokemon(value):
   #New Window
   new_screen = Toplevel()
   new_screen.geometry('620x400')

   #get pokemon
   pokemon = pypokedex.get(name=value)

   #GET IMAGE
   http = urllib3.PoolManager()
   response = http.request('GET', pokemon.sprites.front.get('default'))
   image = PIL.Image.open(BytesIO(response.data))  
   
   #pokemon Information
   pokemon_img = Label(new_screen)
   pokemon_information = Label(new_screen, text=f'{pokemon.dex} - {pokemon.name}', font=('Arial', 12))
   pokemon_type = Label(new_screen, text=f'Type: {pokemon.types}',  font=('Arial', 12))
   pokemon_baseStats = Label(new_screen, text=f'{pokemon.base_stats}', font=('Arial', 12))
   pokemon_weight = Label(new_screen, text=f'Weight: {pokemon.weight}', font=('Arial', 12))
   pokemon_height = Label(new_screen, text=f'Height: {pokemon.height}', font=('Arial', 12))
   

   #POSITIONS   
   pokemon_information.place(x=0, y=120)
   pokemon_type.place(x=0, y=150)
   pokemon_baseStats.place(x=0, y=180)
   pokemon_weight.place(x=0, y=210)
   pokemon_height.place(x=0, y=235)
   pokemon_img.place(x=120, y=30)

   #Put image
   img = PIL.ImageTk.PhotoImage(image)
   pokemon_img.config(image=img)
   pokemon_img.image = img
   
   
# get value of input
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
btn = Button(screen, text='Load Pokemon',command=lambda: LoadPokemon(getValueInput()))
btn.pack()
btn.place(x=100, y=220)


screen.mainloop()

