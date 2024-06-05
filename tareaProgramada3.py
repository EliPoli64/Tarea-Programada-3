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

def opcionCorreo(interfaz,nombrePokemon,pts):
    if nombrePokemon=="mr-mime":
        nombrePokemon="Mr. Mime"
    else:
        nombrePokemon=nombrePokemon.capitalize()
    enviarCorreo(nombrePokemon,pts)
    return salirMenu(interfaz)

def pokemonAtrapado(interfaz,pts,nombrePokemon,tuplaPokemon):
    interfaz.destroy()
    interfaz = Tk()
    listaJugador=cargarPersonaje()
    listaJugador[0]=listaJugador[0]+pts
    grabarPersonaje(listaJugador)
    agregarCapturado(tuplaPokemon)
    interfaz.resizable(False,False)
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center')
    fondo=PhotoImage(file="atrapado.png")
    Label(interfaz, image=fondo).place(x=0, y=0)
    interfaz.title("¡Atrapado!")
    if nombrePokemon=="mr-mime":
        nombrePokemon="Mr. Mime"
        Label(interfaz, text="Mr. Mime",font=("Arial", 20),bg="#EFE4B0").place(x=40, y=35)
    else:
        Label(interfaz, text=nombrePokemon.capitalize(),font=("Arial", 20),bg="#EFE4B0").place(x=40, y=35)
    Label(interfaz, text="¡"+nombrePokemon.capitalize()+" ha sido capturado!",font=("Arial", 16),
          bg="#C3C3C3").place(x=15,y=205)
    Label(interfaz, text=pts,font=("Arial", 20),bg="#EFE4B0").place(x=158, y=76)
    Button(interfaz, text="Compartir",font=("Arial",20),
           command=lambda:opcionCorreo(interfaz,nombrePokemon,pts)).place(x=40,y=250)
    Button(interfaz, text="Salir", font=("Arial",20),
           command=lambda:salirMenu(interfaz)).place(x=440,y=250)
    interfaz.mainloop()
    return ""

def opcionAtrapar(interfaz,nombrePokemon,pts,listaJugador,index,baya,tuplaPokemon):
    if listaJugador[index]<=0:
        print("no iohajcb")
        return messagebox.showwarning(title="No te quedan Pokéballs",message="¡No tienes esas Pokéballs!")
    listaJugador[index]=listaJugador[index]-1
    grabarPersonaje(listaJugador)
    if decidirCaptura(pts,index,baya):
        messagebox.showinfo(title="¡Ya está!",message="¡Pokémon capturado!")
        return pokemonAtrapado(interfaz,pts,nombrePokemon,tuplaPokemon)
    messagebox.showinfo(title="¡Fracaso!",message="¡El Pokémon se ha escapado!")
    return menuAtrapar(interfaz,baya,tuplaPokemon)

def tirarBaya(interfaz,listaJugador,tuplaPokemon):
    if listaJugador[5]<=0:
        return messagebox.showwarning(title="No te quedan Bayas",message="¡No tienes Bayas!")
    listaJugador[5]=listaJugador[5]-1
    grabarPersonaje(listaJugador)
    return menuAtrapar(interfaz,True,tuplaPokemon)

def preAtrapar(interfaz):
    interfaz.destroy()
    interfaz=Tk()
    tuplaPokemon=encontrarPokemon()
    return menuAtrapar(interfaz,False,tuplaPokemon)

def menuAtrapar(interfaz,baya,tuplaPokemon):
    listaJugador=cargarPersonaje()
    interfaz.title("Atrapar Pokémon")
    interfaz.resizable(False,False)
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    fondo=PhotoImage(file="encuentro.png")
    imagenPokemon=obtenerImagen(tuplaPokemon[0],tuplaPokemon[-1])
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
    Label(interfaz, text="Pokéballs: "+str(listaJugador[1]),bg="#C3C3C3").place(x=20,y=210)
    Label(interfaz, text="Superballs: "+str(listaJugador[2]),bg="#C3C3C3").place(x=20,y=230)
    Label(interfaz, text="Ultraballs: "+str(listaJugador[3]),bg="#C3C3C3").place(x=20,y=250)
    Label(interfaz, text="Masterballs: "+str(listaJugador[4]),bg="#C3C3C3").place(x=20,y=270)
    Label(interfaz, text="Bayas: "+str(listaJugador[5]),bg="#C3C3C3").place(x=20,y=290)
    Button(interfaz, text="Huir",command=lambda:huirBatalla(interfaz),font=("Arial", 20)).place(x=455,y=238)
    Button(interfaz, image=imgPoke, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,1,baya,tuplaPokemon)).place(x=300,y=210)
    Button(interfaz, image=imgSuper, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,2,baya,tuplaPokemon)).place(x=350,y=210)
    Button(interfaz, image=imgUltra, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,3,baya,tuplaPokemon)).place(x=300,y=270)
    Button(interfaz, image=imgMaster, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,4,baya,tuplaPokemon)).place(x=350,y=270)
    Button(interfaz, image=imgBaya, relief="flat", 
           command=lambda:tirarBaya(interfaz,listaJugador,tuplaPokemon)).place(x=400,y=240)
    interfaz.mainloop()
    return

def menuPokedex(interfaz):
    archivo=open("pokemon.txt","r")
    lista=archivo.readline().split(",")
    archivo.close()
    interfaz.destroy()
    interfaz = Tk()
    interfaz.title("Pokédex")
    interfaz.resizable(True,True)
    #interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    i=1
    listaPokes=cargarBaseModificable()
    diccImagenes={}
    while i <= len(lista):
        try:
            diccImagenes[i]=obtenerImagen(listaPokes[i-1][0],False)
            if listaPokes[i-1][0]=="mr-mime":
                Label(interfaz, text="Mr. Mime").grid(column=(i-1)%7,row=i//7+2)
            else:
                Label(interfaz, text=listaPokes[i-1][0].capitalize()).grid(column=(i-1)%7,row=i//7+2)
        except:
            diccImagenes[i]=PhotoImage(file="noEncontrado.png")
            Label(interfaz, text="No encontrado").grid(column=(i-1)%7,row=i//7+2)
        Label(interfaz, image = diccImagenes[i]).grid(column=(i-1)%7,row=i//7+1)
        i+=1
        print("ksndc")
    Button(interfaz, text="Salir", font=("Arial",16),
           command=lambda:salirMenu(interfaz)).place(x=440,y=250)
    interfaz.mainloop()
    return 

def opcionComprar(interfaz,listaJugador,index):
    listaJugador = comprarItem(listaJugador, index)
    return menuTienda(interfaz)

def menuTienda(interfaz):
    listaJugador=cargarPersonaje()
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
    Label(interfaz, text=str(listaJugador[0]),bg="#F0D7B7").place(x=362,y=104)
    Button(interfaz, image=imgPoke, relief="flat",
                    command=lambda:opcionComprar(interfaz,listaJugador,1)).place(x=112,y=160)
    Label(interfaz, text="Pokéball\nPrecio: 100pts").place(x=95, y=200)   
    Button(interfaz, image=imgSuper, relief="flat",
                    command=lambda:opcionComprar(interfaz,listaJugador,2)).place(x=262,y=160)
    Label(interfaz,text="Súperball\nPrecio: 300pts").place(x=245, y=200)
    Button(interfaz, image=imgUltra, relief="flat",
                    command=lambda:opcionComprar(interfaz,listaJugador,3)).place(x=412,y=160)
    Label(interfaz, text= "Ultraball\nPrecio: 900pts").place(x=395, y=200)
    Button(interfaz, image=imgMaster, relief="flat",
                    command=lambda:opcionComprar(interfaz,listaJugador,4)).place(x=182,y=230)
    Label(interfaz, text="Masterball\nPrecio: 18000pts").place(x=162, y=270)
    Button(interfaz, image=imgBaya, relief="flat",
                    command=lambda:opcionComprar(interfaz,listaJugador,5)).place(x=342,y=220)
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
    fondo=PhotoImage(file="creditos.png")
    #Créditos con pokefont
    Label(interfaz, image=fondo).place(x=0, y=0)
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "Elaborado por Lindsay Nahome Marín Sánchez\ny Elías Ramírez Hernández").place(x=15, y=170)
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "Información recopilada de PokéAPI").place(x=15, y=200)
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "Sprites de objetos conseguidos de los archivos de"+
          "\nPokémon, en internet",).place(x=15, y=110) # Línea dividida 
    Button(interfaz, text="Salir",
           command=lambda:salirMenu(interfaz)).place(x=460,y=250)
    interfaz.mainloop()
    return ""

def menuPrincipal():
    interfaz=Tk()
    interfaz.resizable(False,False)
    fondo=PhotoImage(file="banner.png")
    interfaz.title("Simulador de encuentro")
    interfaz.geometry("550x320")
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    Label(interfaz, image=fondo).place(x=0, y=0)
    Button(interfaz, text="Atrapar",font=("Arial", 20), 
           command=lambda:preAtrapar(interfaz)).place(x=40,y=15)
    Button(interfaz, text="Pokédex",font=("Arial", 20), 
           command=lambda:menuPokedex(interfaz)).place(x=215,y=15)
    Button(interfaz, text="Tienda",font=("Arial", 20), 
           command=lambda:menuTienda(interfaz)).place(x=409,y=15)
    Button(interfaz, text="Créditos",font=("Arial", 20), 
           command=lambda:menuCreditos(interfaz)).place(x=45,y=250)
    Button(interfaz, text="Salir",font=("Arial", 20), 
           command=lambda:interfaz.destroy()).place(x=430,y=250)
    interfaz.mainloop()
    return ""

grabarBaseEstatica()
try:
    listaListas = cargarBaseModificable()
except FileNotFoundError:
    listaListas= grabarBaseModificable([])

try:
    listaJugador=cargarPersonaje()
    if listaJugador==[0,0,0,0,0,0]:
        listaJugador=[300,10,0,0,0,0] # Evita que el jugador se atasque y quede sin recursos
except:
    listaJugador=[300,10,0,0,0,0]
    grabarPersonaje(listaJugador)
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