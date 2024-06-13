# Elaborado por: Elías Ramírez Hernández y Lindsay Nahome Marín Sánchez
# Fecha de creación 31-05-2024 10:30am
# Última modificación: 03-06-2024 9:03pm
# Versión: 3.12.4

# Importación de librerías

from tkinter import *
from funciones import *
from clases import *
from tkinter import messagebox
from PIL import ImageTk
import re

# Variables globales

interfaz=Tk()   # Interfaz global
icono=PhotoImage(file="logo.png")  # Imagen del programa
interfaz.iconphoto(True, icono)  # Set al icono del programa
interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
interfaz.destroy() 

# Funciones

def salirMenu(interfaz):
    """
    Funcionalidad: Regresa al menú principal de la aplicación
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -menuPrincipal(función)
    """
    interfaz.destroy()
    return menuPrincipal()

def crearVentana(interfaz:Tk):
    """
    Funcionalidad: Crea una nueva ventana.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -interfaz(TkObject): La ventana que se está mostrando.
    """
    interfaz.destroy()
    interfaz = Tk()
    interfaz.eval('tk::PlaceWindow . center') # Coloca la ventana en el centro de la pantalla
    interfaz.title("Simulador de encuentro")
    interfaz.resizable(False,False)
    interfaz.geometry("550x320")
    return interfaz

def huirBatalla(interfaz):
    """
    Funcionalidad: llama a una messagebox que muestra un mensaje de huida y retorna al menú principal.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -menuPrincipal(función)
    """
    messagebox.showinfo(title="Huida",message="¡Escapaste sin problemas!")
    tocarMusicaMenu()
    interfaz.destroy()
    return menuPrincipal()

def enviarCorreoAux(interfaz,correoElectronico:str,nombrePokemon,pts):
    """
    Funcionalidad: Valida el correo seleccionado.
    Entrada:
    -correoElectronico(str): Correo que el usuario insertó en la función opcionCorreo.
    -nombrePokemon(str): Nombre del Pokémon a enviar.
    -pts(int): número de puntos que dio el Pokémon atrapado.
    Salida:
    -enviarCorreo(función): Envía el correo ya validado.
    """
    if not re.search(r"@{1}\w+.{1}\w+.*\w*", correoElectronico):
        return messagebox.showerror(title="Error", message= "El correo no sigue un formato válido.")
    posArroba = correoElectronico.find("@")
    print(correoElectronico[posArroba+1:])
    if correoElectronico[posArroba+1:] not in terminacionCorreo:
        return messagebox.showerror(title="Error", message= "El correo no tiene una terminación válida.")
    try:
        enviarCorreo(correoElectronico,nombrePokemon,pts)
    except:
        messagebox.showerror(title="Error", message= "El correo ingresado no es válido.")
    return salirMenu(interfaz)

def opcionCorreo(interfaz:Tk,nombrePokemon,pts):
    """
    Funcionalidad: llama a la función enviarCorreo que envía un correo electrónico con información 
    del Pokémon atrapado y llama al menú principal.
    Entradas:
    -interfaz(TkObject): La ventana que se está mostrando.
    -nombrePokemon(str): Nombre del Pokémon a enviar.
    -pts(int): número de puntos que dio el Pokémon atrapado.
    Salida:
    -menuPrincipal(función)
    """
    interfaz.destroy()
    interfaz=Tk()
    interfaz.title("Enviar correo electrónico")
    interfaz.eval('tk::PlaceWindow . center')
    if nombrePokemon=="mr-mime":
        nombrePokemon="Mr. Mime"
    else:
        nombrePokemon=nombrePokemon.capitalize()
    Label(interfaz, text="Ingrese el correo al que quiere enviar, permite solo\n"+
          "Gmail, Hotmail, Outlook, Racsa y Estudiantec:").grid(row=0,column=0)
    correo=Entry(interfaz)
    correo.grid(row=0,column=1)
    Button(interfaz,text="Confirmar", font=("Arial",12),
           command=lambda:enviarCorreoAux(interfaz,correo.get(),nombrePokemon,pts)).grid(row=1,column=1)
    Button(interfaz, text="Salir", font=("Arial",12),
           command=lambda:salirMenu(interfaz)).grid(row=1, column=0)
    return ""

def pokemonAtrapado(interfaz,pts,nombrePokemon,tuplaPokemon):
    """
    Funcionalidad: muestra la ventana en la que el Pokémon está atrapado.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    -nombrePokemon(str): Nombre del Pokémon a enviar.
    -pts(int): número de puntos que dio el Pokémon atrapado.
    -tuplaPokemon(tuple): Tupla con la información del Pokémon.
    Salida:
    -menuPrincipal(función)
    """
    tocarMusicaMenu()
    listaJugador=cargarPersonaje()
    listaJugador[0]=listaJugador[0]+pts
    grabarPersonaje(listaJugador)
    agregarCapturado(tuplaPokemon)
    interfaz=crearVentana(interfaz)
    fondo=PhotoImage(file="atrapado.png")
    Label(interfaz, image=fondo).place(x=0, y=0)
    interfaz.title("¡Atrapado!")
    if nombrePokemon=="mr-mime":
        nombrePokemon="Mr. Mime"
        Label(interfaz, text="Mr. Mime",font=("Arial", 20),bg="#EFE4B0").place(x=40, y=35)
        Label(interfaz, text="¡Mr. Mime ha sido capturado!",font=("Arial", 16),
            bg="#C3C3C3").place(x=15,y=205)
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

def opcionAtrapar(interfaz:Tk,nombrePokemon:str,pts:int,listaJugador:list,index:int,baya:bool,tuplaPokemon:tuple,fotoPokemon:Image):
    """
    Funcionalidad:
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    -nombrePokemon(str): Nombre del Pokémon a enviar.
    -pts(int): número de puntos que dio el Pokémon atrapado.
    -listaJugador(list):
    -index(int): Index de la Pokéball gastada.
    -baya(bool): Indica si el Pokémon a atrapar está bajo la influencia de una baya.
    -tuplaPokemon(tuple): Una tupla con tres características del pokémon: Nombre, puntos y atributo de shiny.
    Salida:
    -pokemonAtrapado(función): Si el Pokémon fue atrapado graba los datos con la función.
    -Messagebox(TkObject): Indica que el usuario no tiene Pokéballs de ese tipo.
    -menuAtrapar(función): Si el Pokémon se escapó.
    """
    if listaJugador[index]<=0:
        return messagebox.showwarning(title="No te quedan Pokéballs",message="¡No tienes esas Pokéballs!")
    listaJugador[index]=listaJugador[index]-1
    grabarPersonaje(listaJugador)
    if decidirCaptura(pts,index,baya):
        messagebox.showinfo(title="¡Ya está!",message="¡Pokémon capturado!")
        return pokemonAtrapado(interfaz,pts,nombrePokemon,tuplaPokemon)
    messagebox.showinfo(title="¡Fracaso!",message="¡El Pokémon se ha escapado!")
    return menuAtrapar(interfaz,baya,tuplaPokemon,fotoPokemon)

def tirarBaya(interfaz:Tk,listaJugador:list,tuplaPokemon:tuple,fotoPokemon:Image):
    """
    Funcionalidad: Tira una baya al Pokémon para aumentar su posibilidad de ser atrapado.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    -listaJugador(list): Una lista con la información del jugador (puntaje, cantidad de pokéballs y bayas).
    -tuplaPokemon(tuple): Una tupla con tres características del pokémon: Nombre, puntos y atributo de shiny.
    Salida:
    -Messagebox(TkObject): Indica que el usuario no tiene Bayas.
    -menuPrincipal(función)
    """
    if listaJugador[5]<=0:
        return messagebox.showwarning(title="No te quedan Bayas",message="¡No tienes Bayas!")
    listaJugador[5]=listaJugador[5]-1
    grabarPersonaje(listaJugador)
    return menuAtrapar(interfaz,True,tuplaPokemon,fotoPokemon)

def preAtrapar(interfaz:Tk):
    """
    Funcionalidad: Genera un encuentro aleatorio con un pokémon e inicializa los valores para este.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -menuAtrapar(función)
    """
    tocarMusicaEncuentro()
    tuplaPokemon=encontrarPokemon()
    return menuAtrapar(interfaz,False,tuplaPokemon,obtenerImagen(tuplaPokemon[0],tuplaPokemon[2]))

def menuAtrapar(interfaz:Tk,baya:bool,tuplaPokemon:tuple,fotoPokemon:Image):
    """
    Funcionalidad: Muestra el menú de encuentro con un pokémon para ser atrapado.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    -baya(bool): Indica si el Pokémon a atrapar está bajo la influencia de una baya.
    -tuplaPokemon(tuple): Una tupla con tres características del pokémon: Nombre, puntos y atributo de shiny.
    Salida:
    -menuPrincipal(función)
    """
    listaJugador=cargarPersonaje()
    interfaz = crearVentana(interfaz) # Coloca la ventana en el centro de la pantalla
    fondo=PhotoImage(file="encuentro.png")
    imagenPokemon=ImageTk.PhotoImage(fotoPokemon)
    Label(interfaz, image=fondo).place(x=0, y=0)
    if tuplaPokemon[0]=="mr-mime":
        Label(interfaz, text="Mr. Mime",font=("Arial", 20),bg="#EFE4B0").place(x=40, y=35)
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
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,1,baya,tuplaPokemon,fotoPokemon)).place(x=300,y=210)
    Button(interfaz, image=imgSuper, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,2,baya,tuplaPokemon,fotoPokemon)).place(x=350,y=210)
    Button(interfaz, image=imgUltra, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,3,baya,tuplaPokemon,fotoPokemon)).place(x=300,y=270)
    Button(interfaz, image=imgMaster, relief="flat", 
           command=lambda:opcionAtrapar(interfaz,tuplaPokemon[0],tuplaPokemon[1],listaJugador,4,baya,tuplaPokemon,fotoPokemon)).place(x=350,y=270)
    Button(interfaz, image=imgBaya, relief="flat", 
           command=lambda:tirarBaya(interfaz,listaJugador,tuplaPokemon,fotoPokemon)).place(x=400,y=240)
    interfaz.mainloop()
    return

def menuPokedex(interfaz:Tk):
    """
    Funcionalidad: Muestra el menú de la tienda pokédex.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -N/A
    """
    archivo=open("pokemon.txt","r")
    lista=archivo.readline().split(",")
    archivo.close()
    interfaz.destroy()
    interfaz=Tk()
    interfaz.title("Simulador de encuentro")
    i=1
    listaPokes=cargarBaseModificable()
    listaCargados=[]
    diccImagenes={}
    fondo=PhotoImage(file="pokedex.png")
    Label(interfaz, image=fondo).place(x=0, y=0)
    cuenta=1
    completada=True
    while i<=len(lista) or cuenta<=len(lista): 
        try:
            if listaPokes[i-1][0] not in listaCargados:
                diccImagenes[i]=ImageTk.PhotoImage((obtenerImagen(listaPokes[i-1][0],False)))
                if listaPokes[i-1][0]=="mr-mime":
                    Label(interfaz, text="Mr. Mime").grid(column=(cuenta-1)%6,row=((cuenta-1)//6)*2+2)
                    listaCargados.append(listaPokes[i-1][0])
                else:
                    Label(interfaz, text=listaPokes[i-1][0].capitalize()).grid(column=(cuenta-1)%6,row=((cuenta-1)//6)*2+2) #Tag
                    listaCargados.append(listaPokes[i-1][0])
                Label(interfaz, image = diccImagenes[i]).grid(column=(cuenta-1)%6,row=((cuenta-1)//6)*2+1) # Imagen
                print("Generados: "+str(cuenta))
                cuenta+=1
        except:
            diccImagenes[i]=PhotoImage(file="noEncontrado.png")
            completada=False
            Label(interfaz, text="No encontrado").grid(column=(cuenta-1)%6,row=((cuenta-1)//6)*2+2) # Tag
            Label(interfaz, image = diccImagenes[i]).grid(column=(cuenta-1)%6,row=((cuenta-1)//6)*2+1) # Imagen
            print("Generados: "+str(cuenta))
            cuenta+=1
        i+=1
    Label(interfaz,text="\n\n\n\n\n",bg="#DA1E2D").grid(column=0,row=0)
    Button(interfaz, text="Salir", font=("Arial",16),
           command=lambda:salirMenu(interfaz)).grid(column=5,row=9)
    if completada:
        tocarYippee()
        tocarMusicaMenu()
        messagebox.showinfo(title= "¡Felicidades!", message= "¡Completaste la Pokédex!\n¡Gracias por jugar!")
    interfaz.mainloop()
    return 

def opcionComprar(interfaz,listaJugador,index):
    """
    Funcionalidad: Refresca la ventana para mostrar el cambio en las estadísticas después
    de una compra.
    Entradas:
    -interfaz(TkObject): La ventana que se está mostrando.
    -listaJugador(list): Una lista con la información del jugador (puntaje, cantidad de pokeballs y bayas).
    -index(int): El índice del objeto que fue comprado.
    Salida:
    -menuTienda(función)
    """
    listaJugador = comprarItem(listaJugador, index)
    return menuTienda(interfaz)

def menuTienda(interfaz):
    """
    Funcionalidad: Muestra el menú de la tienda pokémon.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -N/A
    """
    listaJugador=cargarPersonaje()
    interfaz = crearVentana(interfaz)
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
    """
    Funcionalidad: Muestra los créditos de la aplicación.
    Entrada:
    -interfaz(TkObject): La ventana que se está mostrando.
    Salida:
    -N/A
    """
    interfaz = crearVentana(interfaz)
    fondo=PhotoImage(file="creditos.png")
    Label(interfaz, image=fondo).place(x=0, y=0)
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "Elaborado por Lindsay Nahome Marín Sánchez y Elías Ramírez Hernández.").place(x=15, y=155)
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "Información recopilada de PokéAPI.").place(x=15, y=200)
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "Sprites de objetos conseguidos de los archivos de los juegos de"+
          " Pokémon.").place(x=15, y=110) # Línea dividida 
    Label(interfaz,bg="#EFE4B0",font=("Segoe UI",10),
          text= "¡Gracias por utilizar nuestra tarea!").place(x=15, y=245)
    Button(interfaz, text="Salir",
           command=lambda:salirMenu(interfaz), font=("Arial", 16)).place(x=460,y=250)
    interfaz.mainloop()
    return ""

def menuPrincipal():
    """
    Funcionalidad: El menú principal de la aplicación. Muestra los botones con las diferentes 
    funciones que tiene el programa.
    Entrada:
    -N/A
    Salida:
    -N/A
    """
    interfaz = crearVentana(interfaz=Tk())
    fondo=PhotoImage(file="banner.png")
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

# Programa principal
try:
    diccPokes=compararBasesDatos()
except FileNotFoundError:
    diccPokes=grabarBaseEstatica()
try:
    listaListas = cargarBaseModificable()
except FileNotFoundError:
    listaListas= grabarBaseModificable([])
try:
    listaJugador=cargarPersonaje()
    if listaJugador==[0,0,0,0,0,0]:
        listaJugador=[300,10,0,0,0,0] # Evita que el jugador se atasque y quede sin recursos
except:
    listaJugador=[300,10,0,0,10000,0]
    grabarPersonaje(listaJugador)
tocarMusicaMenu()
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