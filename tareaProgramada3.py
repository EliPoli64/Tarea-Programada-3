# Elaborado por: Elías Ramírez Hernández y Lindsay Nahome Marín Sánchez
# Fecha de creación 24-05-2024 10:30am
# Última modificación: 03-06-2024 9:03pm
# Versión: 3.12.3

# Importación de librerías

from tkinter import *
from funciones import *
from clases import *
import playsound
from tkinter import messagebox

# Atrapar-Pokedex-Tienda-Créditos-Salir

def salirMenu(interfaz):
    interfaz.destroy()
    return menuPrincipal()

def crearVentana(interfaz):
    interfaz.destroy()
    interfaz = Tk()
    interfaz.title("Simulador de encuentro")
    interfaz.resizable(False,False)
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    return interfaz

def huirBatalla(interfaz):
    messagebox.showinfo(title="Huida",message="¡Escapaste sin problemas!")
    interfaz.destroy()
    return menuPrincipal()

def menuAtrapar(interfaz):
    interfaz.destroy()
    interfaz=Tk()
    tuplaPokemon=encontrarPokemon()
    interfaz.title("Atrapar Pokémon")
    interfaz.resizable(False,False)
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    fondo=PhotoImage(file="encuentro.png")
    imagenPokemon=tuplaPokemon[-1]
    Label(interfaz, image=fondo).place(x=0, y=0)
    if tuplaPokemon[0]=="mr-mime":
        Label(interfaz, text="Mr. Mime",font=("Arial", 20)).place(x=40, y=35)
    else:
        Label(interfaz, text=tuplaPokemon[0].capitalize(),font=("Arial", 20),bg="#EFE4B0").place(x=40, y=35)
    Label(interfaz, text=tuplaPokemon[1],font=("Arial", 20),bg="#EFE4B0").place(x=158, y=76)
    Label(interfaz,image=imagenPokemon).place(x=359,y=70)
    imgPoke=PhotoImage(file="poke.png")
    imgSuper=PhotoImage(file="super.png")
    imgUltra=PhotoImage(file="ultra.png")
    imgMaster=PhotoImage(file="master.png")
    imgBaya=PhotoImage(file="baya.png")
    Button(interfaz, text="Huir",command=lambda:huirBatalla(interfaz),font=("Arial", 20)).place(x=455,y=238)
    Button(interfaz, image=imgPoke, relief="flat", command=lambda:menuAtrapar()).place(x=300,y=210)
    Button(interfaz, image=imgSuper, relief="flat", command=lambda:menuAtrapar()).place(x=350,y=210)
    Button(interfaz, image=imgUltra, relief="flat", command=lambda:menuAtrapar()).place(x=300,y=270)
    Button(interfaz, image=imgMaster, relief="flat", command=lambda:menuAtrapar()).place(x=350,y=270)
    Button(interfaz, image=imgBaya, relief="flat", command=lambda:menuAtrapar()).place(x=400,y=240)
    interfaz.mainloop()
    return

def menuPokedex(interfaz):
    return 

def menuTienda(interfaz):
    interfaz.destroy()
    interfaz=Tk()
    interfaz.resizable(False,False)
    interfaz.title("Simulador de encuentro")
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    fondo=PhotoImage(file="tienda.png")
    Label(interfaz, image=fondo).place(x=0, y=0)
    imgPoke=PhotoImage(file="poke.png")
    imgSuper=PhotoImage(file="super.png")
    imgUltra=PhotoImage(file="ultra.png")
    imgMaster=PhotoImage(file="master.png") 
    imgBaya = PhotoImage(file="baya.png") # Importar imágenes
    Button(interfaz, image=imgPoke, relief="flat",command=lambda:menuAtrapar()).place(x=112,y=160)
    Label(interfaz, text="Pokéball\nPrecio: 100pts").place(x=95, y=200)   
    Button(interfaz, image=imgSuper, relief="flat",command=lambda:menuAtrapar()).place(x=262,y=160)
    Label(interfaz,text="Súperball\nPrecio: 300pts").place(x=245, y=200)
    Button(interfaz, image=imgUltra, relief="flat",command=lambda:menuAtrapar()).place(x=412,y=160)
    Label(interfaz, text= "Ultraball\nPrecio: 900pts").place(x=395, y=200)
    Button(interfaz, image=imgMaster, relief="flat",command=lambda:menuAtrapar()).place(x=182,y=230)
    Label(interfaz, text="Masterball\nPrecio: 18000pts").place(x=162, y=270)
    Button(interfaz, image=imgBaya, relief="flat",command=lambda:menuAtrapar()).place(x=342,y=220)
    Label(interfaz, text="Baya\nPrecio: 300pts").place(x=322, y=270)
    Button(interfaz, text="Salir",font=("Arial", 20),
           command=lambda:salirMenu(interfaz)).place(x=460,y=250)
    interfaz.mainloop()
    return 

def menuCreditos(interfaz):
    interfaz.destroy()
    interfaz=Tk()
    interfaz.resizable(False,False)
    interfaz.title("Simulador de encuentro")
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    #Créditos con pokefont
    Label(interfaz, text= "Creado por:\n Elías Ramírez Hernández\nLindsay Nahome Marín Sánchez").place(x=180, y=50)
    Label(interfaz, text= "Información recopilada de PokeAPI").place(x=180, y=70)
    Label(interfaz, text= "Sprites de pokéball, superball, ultraball y masterball conseguidos de:"+
          "\nPokémon Blanco y Negro",).place(x=395, y=80)

def menuPrincipal():
    interfaz=Tk()
    interfaz.resizable(False,False)
    fondo=PhotoImage(file="banner.png")
    interfaz.title("Simulador de encuentro")
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    Label(interfaz, image=fondo).place(x=0, y=0)
    Button(interfaz, text="Atrapar", command=lambda:menuAtrapar(interfaz)).place(x=40,y=15)
    Button(interfaz, text="Pokédex", command=lambda:menuPokedex(interfaz)).place(x=257.5,y=15)
    Button(interfaz, text="Tienda", command=lambda:menuTienda(interfaz)).place(x=475,y=15)
    Button(interfaz, text="Créditos", command=lambda:menuCreditos(interfaz)).place(y=280,x=40)
    Button(interfaz, text="Salir", command=lambda:interfaz.destroy(interfaz)).place(x=475,y=280)
    interfaz.mainloop()
    return ""


grabarBaseEstatica()
menuPrincipal()






"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠞⠛⠛⠉⠉⠛⠛⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⣠⡖⢠⠀⠀⠀⠀⠀⠀⠀⠀⣧⣼⣷⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⢠⢿⣷⣶⡇⠀⠀⠀⠀⠀⠀⠀⡿⣿⡿⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣇⠀⠀⢸⠸⠻⡿⠇⠀⠀⠀⠀⠀⠀⠀⠐⠒⠈⢀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⡀⣿⠀⠀⠀⠁⠀⠉⠁⢀⣀⣀⣀⣄⣤⠴⢶⣶⣿⡏⠀⣸⣃⣀⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣾⠉⠛⠛⠦⠤⣄⡀⢿⡋⠉⠉⠁⠀⠀⠉⠁⠀⠀⢈⡟⢀⡼⠛⠉⠉⠉⠉⠉⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣦⣀⠀⣀⣠⠤⠖⠒⠒⢛⣛⣻⣷⡖⣀⡀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡋⢉⣠⠴⠖⠚⠉⠉⠁⠉⠻⣍⣹⣶⣦⣀⡀⠀⠀⣸⣷⠶⠶⠶⠶⢦⣤⣴⣦⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⣀⠀⠀⠀⠀⣀⣠⠤⠖⠛⠙⢿⣄⠈⠉⠙⠻⢿⣇⠀⠀⠀⠀⢠⠟⠀⠘⠛⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⢦⣄⡀⠀⠀⠀⠀⣠⣏⡉⠉⠉⠉⢉⡿⠟⠒⠒⠤⣄⡀⠀⠉⢦⡀⠀⠀⠀⠉⢧⠀⠀⠀⠋⠀⠀⠀⠀⠀⠉⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⢷⣶⣿⣿⣭⣭⡉⠑⢦⣴⠃⠀⠀⠀⠀⠀⠀⣙⣦⣠⣄⡹⢦⣀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣁⣀⣠⣤⣄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣆⠘⡇⠀⠀⠀⠀⣶⠶⠞⠉⠛⠋⠘⣇⠀⠈⠳⢦⡀⠘⡆⠀⠀⠀⠀⠀⠀⠀⣰⠟⠋⠁⠀⠀⠀⠉⠙⠳⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⡄⣧⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠙⠳⡿⣶⣶⣤⣀⣀⣠⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⡘⢧⡀⠀⠀⢿⠀⠀⠀⠀⠀⠀⣼⠀⢀⣠⣤⣄⡼⠁⣼⠀⠀⠉⠉⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⡉⠓⠦⠼⣧⡀⠀⠀⠀⣰⡇⢠⠋⠀⠀⠀⠙⠶⣯⣀⠀⠀⠀⣿⠀⠀⠀⠀⡴⠚⠛⠳⣆⠀⠀⠀⠀⠸⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣽⣶⣶⣾⣉⣉⠙⣄⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠻⡆⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⢰⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠶⢤⡤⠴⠛⠁⠀⠀⠀⢠⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠶⣦⣤⣤⣀⣀⣀⣀⣠⣤⡴⠾⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀

"""