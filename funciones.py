# Elaborado por: Elías Ramírez Hernández y Lindsay Nahome Marín Sánchez
# Fecha de creación 31-05-2024 10:30am
# Última modificación: 03-06-2024 9:03pm
# Versión: 3.12.3

# Importación de librerías

import pokebase as pb
import pickle
import pygame
import random
from PIL import Image
import requests
from io import BytesIO
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
from clases import *
from playsound import playsound

# Variables globales
terminacionCorreo= ("gmail.com","outlook.com","hotmail.com","racsa.go.cr","estudiantec.cr")

# Definición de funciones

def tocarMusicaEncuentro():
    """
    Funcionalidad: Toca la música para los encuentros.
    Entrada:
    -N/A
    Salida:
    -pygame.mixer.music.play(objeto Pygame): Reproduce la música del encuentro en ciclo 5 veces.
    """
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("musicaBatalla.mp3")
    return pygame.mixer.music.play(loops=5)

def tocarMusicaMenu():
    """
    Funcionalidad: Toca la música para los menús.
    Entrada:
    -N/A
    Salida:
    -pygame.mixer.music.play(objeto Pygame): Reproduce la música del menú en ciclo 15 veces.
    """
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.4)
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("musicaMenus.mp3")
    except:
        pygame.mixer.music.load("musicaMenus.mp3")
    return pygame.mixer.music.play(loops=15)

def tocarCompleta():
    """
    Funcionalidad: Toca un sonido para felicitar al usuario por terminar la pokédex.
    Entrada:
    -N/A
    Salida:
    -pygame.mixer.music.play(objeto Pygame): Reproduce un efecto de sonido de felicitación.
    """
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("pokedexCompleta.mp3")
    return pygame.mixer.music.play(loops=1)

def grabarBaseEstatica():
    """
    Funcionalidad: Guarda los datos del jugador y los objetos que tiene.
    Entrada:
    -N/A
    Salida:
    -pygame.mixer.music.play(objeto Pygame): Reproduce la música del menú en ciclo 15 veces.
    """
    diccPokes=obtenerPokes()
    baseEstatica=open("baseEstatica.txt","wb")
    pickle.dump(diccPokes,baseEstatica)
    baseEstatica.close()
    return diccPokes
    
def grabarPersonaje(listaJugador):
    """
    Funcionalidad: Guarda los datos del jugador y los objetos que tiene.
    Entrada:
    -listaJugador(list): Una lista con la información del jugador (puntaje, cantidad de pokéballs y bayas).
    Salida:
    -N/A
    """
    datosPersonaje=open("datosJugador.txt","w")
    datosPersonaje.write(str(listaJugador[0])+","+str(listaJugador[1])+","+str(listaJugador[2])+","+
                         str(listaJugador[3])+","+str(listaJugador[4])+","+str(listaJugador[5]))
    datosPersonaje.close()
    return ""

def cargarPersonaje():
    """
    Funcionalidad: Carga los datos del jugador y los objetos que tiene.
    Entrada:
    -N/A
    Salida:
    -listaJugador(list): Una lista con la información del jugador (puntaje, cantidad de pokéballs y bayas).
    """
    datosPersonaje=open("datosJugador.txt","r")
    listaCargada=datosPersonaje.read().split(",")
    i=0
    while i<len(listaCargada):
        listaCargada[i]=int(listaCargada[i])
        i+=1
    datosPersonaje.close()
    return listaCargada

def cargarBaseModificable():
    """
    Funcionalidad: Carga la base de datos modificable, esta es la que tiene la información de los pokémon atrapados.
    Entrada: 
    -N/A
    Salida:
    -listaListas(list): La lista de listas con la información de los pokémon atrapados.
    """
    listaListas=[]
    baseMod = open("baseModificable.txt","rb")
    try:
        listaObj=pickle.load(baseMod)
        for objeto in listaObj:
            listaListas.append([objeto.mostrarNombre(),objeto.mostrarTuplaMedidas(),objeto.mostrarListaTipos(),
                                objeto.mostrarPuntos(), objeto.mostrarEsShiny(),objeto.mostrarImagen()])
        baseMod.close()
    except:
        baseMod.close()
    return listaListas
    
def grabarBaseModificable(pokeActual,valor=True):
    """
    Funcionalidad: Guarda la base de datos modificable, esta es la que tiene la información de los pokémon atrapados.
    Entrada: 
    -listaCapturados(list): La lista de listas con la información de los pokémon atrapados.
    Salida:
    -N/A
    """
    if not valor:
        baseMod = open("baseModificable.txt","wb")
        pickle.dump([],baseMod)
        baseMod.close()
        return ""
    baseMod = open("baseModificable.txt","rb")
    listaCapturados=pickle.load(baseMod)
    baseMod.close()
    baseMod = open("baseModificable.txt","wb")
    pokemonAtr = Pokemon()
    pokemonAtr.asignarNombre(pokeActual[0])
    pokemonAtr.asignarTuplaMedidas(pokeActual[1])
    pokemonAtr.asignarListaTipos(pokeActual[2])
    pokemonAtr.asignarPuntos(pokeActual[3])
    sprite=pb.pokemon(pokeActual[0]).sprites
    if pokeActual[3]//10==300 or pokeActual[3]//10==600 or pokeActual[3]//10==900 or pokeActual[3]//10==1800:
        pokemonAtr.asignarEsShiny(True)
        pokemonAtr.asignarImagen(sprite.front_shiny)
    else:
        pokemonAtr.asignarEsShiny(False)
        pokemonAtr.asignarImagen(sprite.front_default)
    listaCapturados.append(pokemonAtr)        
    pickle.dump(listaCapturados,baseMod)
    baseMod.close()
    return ""

def agregarCapturado(tuplaPokemon):
    """
    Funcionalidad: Agrega el pokémon que fue capturado a la lista de capturados y guarda los cambios.
    Entrada:
    -tuplaPokemon(tuple): Una tupla con la información del pokémon actual.
    Salida:
    -N/A
    """
    baseEst = open("baseEstatica.txt","rb")
    diccPokes=pickle.load(baseEst) #Nombre, puntos y atributo de shiny.
    for key in diccPokes.keys(): # (pokemon,(infoPoke.height*10,infoPoke.weight*10),listaTipos,puntos)
        if diccPokes[key][0]==tuplaPokemon[0]:
            pokeActual=[tuplaPokemon[0],diccPokes[key][1],diccPokes[key][2],tuplaPokemon[1]]
    grabarBaseModificable(pokeActual)
    return ""

def obtenerImagen(nombrePoke,esShiny):
    """
    Funcionalidad: Obtiene la imagen del pokemon desde la API.
    Entradas:
    -nombrePoke(str): El nombre del pokémon actual.
    -esShiny(bool): Determina si el pokémon actual es shiny.
    Salida:
    -(obj): El sprite del pokémon solicitado.
    """
    sprite=pb.pokemon(nombrePoke).sprites
    if esShiny:
        return Image.open(BytesIO(requests.get(sprite.front_shiny).content))
    return Image.open(BytesIO(requests.get(sprite.front_default).content))
                            
def encontrarPokemon(): # diccPokemon[pokemon]=(pokemon,(infoPoke.height*10,infoPoke.weight*10),listaTipos,puntos)
    """
    Funcionalidad: Genera un pokémon aleatorio para el encuentro.
    Entrada:
    -N/A
    Salida:
    -tuplaPokemon(tuple): Una tupla con tres características del pokémon: Nombre, puntos y atributo de shiny.
    """
    baseEstatica=open("baseEstatica.txt","rb")
    diccPokes=pickle.load(baseEstatica)
    numPokemon = random.randint(1,len(diccPokes))
    if random.randint(1,256)==1:
        tuplaPokemon=(diccPokes[numPokemon][0],diccPokes[numPokemon][-1]*10,True)
    else:
        tuplaPokemon=(diccPokes[numPokemon][0],diccPokes[numPokemon][-1],False) 
    baseEstatica.close()
    return tuplaPokemon

def decidirCaptura(pts,index,baya):
    """
    Funcionalidad: Decide si el pokémon será capturado con la pokeball seleccionada.
    Entrada:
    -pts(int): La cantidad de puntos que vale la captura.
    -index(int): Indica la pokéball que fue seleccionada.
    -baya(bool): True si el pokémon ha consumido una baya, False en caso contrario.
    Salida:
    -(bool): Determina si el pokemon se atrapará.
    """
    if index == 1 or index == 2 or index == 3:
        ratioCaptura=index
    else:
        ratioCaptura=20 # masterball
    if str(pts)[0]=="1":
        ratioCaptura*=5
    elif str(pts)[0]=="3":
        ratioCaptura*=75
    elif str(pts)[0]=="6":
        ratioCaptura*=50
    elif str(pts)[0]=="9":
        ratioCaptura*=25
    if baya:
        ratioCaptura*=1.2
    return random.randint(1,100)<=ratioCaptura

def enviarCorreo(correoElectronico,nombrePokemon,pts):
    """
    Funcionalidad: Comparte la información del pokémon atrapado mediante un correo eléctronico.
    Entradas:
    -correoElectronico(str): dirección a la cual se va a enviar el correo electrónico.
    -nombrePokemon(str): El nombre del pokémon actual.
    -pts(int): Cantidad de puntos que proporciona el pokémon.
    Salida:
    -messagebox(TkObject): Una ventana que notifica que el correo se ha enviado con éxito.
    """
    correo=EmailMessage()
    correo.set_content("¡Mira! He atrapado este "+nombrePokemon+" y me dio "+str(pts)+" puntos.")
    correo['Subject'] = "¡He capturado algo! :D"
    correo["From"]="soggycat64@gmail.com"
    correo["To"]=correoElectronico
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    server.set_debuglevel(1)
    server.login("soggycat64@gmail.com", "afhd rgun lrmy drcv")
    server.send_message(correo)
    server.quit()
    return messagebox.showinfo(title="¡Compartido!",message="Se ha enviado el correo con éxito. ¡Felicidades!")

def comprarItem(listaJugador,index):
    """
    Funcionalidad: Resta puntos al jugador a cambio de un objeto de la tienda.
    Entradas:
    -listaJugador(list): Una lista con la información del jugador (puntaje, cantidad de pokeballs y bayas).
    -index(int): El índice del objeto que fue comprado.
    Salida:
    -listaJugador(list): Una lista con la información del jugador (puntaje, cantidad de pokeballs y bayas).
    """
    if index==1:
        if listaJugador[0]<100:
            messagebox.showwarning(title="Error",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-100
    elif index==2 or index==5:
        if listaJugador[0]<300:
            messagebox.showwarning(title="Error",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-300
    elif index==3:
        if listaJugador[0]<900:
            messagebox.showwarning(title="Error",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-900
    else:
        if listaJugador[0]<18000:
            messagebox.showwarning(title="Error",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-18000 
    listaJugador[index]=listaJugador[index]+1
    grabarPersonaje(listaJugador)
    return listaJugador
    
def obtenerPokes(): # rattata,mankey,pidgey,seel,poliwag,eevee,mr-mime,mewtwo,sentret,ekans,mareep,wooper,hoppip,skarmory,swinub,celebi,wurmple,zangoose,poochyena,seedot,ralts,electrike,wingull,rayquaza
    """
    Funcionalidad: Obtiene los pokémon específicados de la API y convierte la información de estos en un diccionario.
    Entrada:
    -N/A
    Salida:
    -diccPokemon(dicc): Un diccionario con la información elemental de cada pokémon.
    """
    archivo=open("pokemon.txt","r")
    lista=archivo.readline().split(",")
    diccPokemon={}
    i=1
    for pokemon in lista:
        listaTipos=[]
        sumaStats=0
        infoPoke=pb.pokemon(pokemon)
        for tipo in infoPoke.types:
            listaTipos.append(tipo.type.name)
        for stat in infoPoke.stats:
            sumaStats+=stat.base_stat
        if sumaStats<300:
            puntos=300
        elif 300<=sumaStats<=400:
            puntos=600
        elif 400<sumaStats<599:
            puntos=900
        else:
            puntos=1800
        diccPokemon[i]=(pokemon,(infoPoke.height*10,infoPoke.weight*10),listaTipos,puntos)
        print("Pokémon cargados: "+str(i))
        i+=1
    archivo.close()
    return diccPokemon

def compararBasesDatos():
    """
    Funcionalidad: Compara las base de datos para verificar si una modificación se hizo
    a la lista de pokémon disponibles.
    Entrada:
    -N/A
    Salidas:
    -N/A
    -grabarBaseEstatica(función)
    """
    baseEst = open("baseEstatica.txt","rb")
    archivo=open("pokemon.txt","r")
    diccPokes:dict=pickle.load(baseEst)
    listaPokes=archivo.readline().split(",")
    for poke in listaPokes:
        estaPoke = False
        for key in diccPokes.keys():
            if diccPokes[key][0]==poke:
                estaPoke=True
        if not estaPoke:
            grabarBaseModificable("a",False)
            baseEst.close()
            archivo.close()
            return grabarBaseEstatica()
    for key in diccPokes.keys():
        estaPoke = False
        for poke in listaPokes:
            if diccPokes[key][0]==poke:
                estaPoke=True
        if not estaPoke:
            grabarBaseModificable("a",False)
            baseEst.close()
            archivo.close()
            return grabarBaseEstatica()
    baseEst.close()
    archivo.close()
    return diccPokes
