import pokebase as pb
import pickle
import playsound
import random
from PIL import ImageTk
from PIL import Image
import requests
from io import BytesIO
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
from clases import *
#Si un Pokémon atrapado tiene menos de 300 en total de estadísticas, da 300pts. Si está
#entre 300 y 400 ambos inclusive dan 600pts. Entre 400 y 599 da 900pts, y 600 o más da
#1800pts.

#Variables globales
#cantPokeball=0
#cantSuperball=0
#cantUltraball=0
#cantMasterball=0
#cantBayas=0
#puntaje=0
#listaJugador = [300,10,0,0,0,0] #puntaje, pokeball, superball, ultraball, masterball, bayas


#Variables globales fin


"""def tocarCancion():
    playsound.playsound() 
"""
def grabarBaseEstatica():
    diccPokes=obtenerPokes()
    baseEstatica=open("baseEstatica.txt","wb")
    pickle.dump(diccPokes,baseEstatica)
    baseEstatica.close()
    return diccPokes
    
def grabarPersonaje(listaJugador):
    datosPersonaje=open("datosJugador.txt","w")
    datosPersonaje.write(str(listaJugador[0])+","+str(listaJugador[1])+","+str(listaJugador[2])+","+
                         str(listaJugador[3])+","+str(listaJugador[4])+","+str(listaJugador[5]))
    datosPersonaje.close()
    return ""

def cargarPersonaje():
    datosPersonaje=open("datosJugador.txt","r")
    listaCargada=datosPersonaje.read().split(",")
    i=0
    while i<len(listaCargada):
        listaCargada[i]=int(listaCargada[i])
        i+=1
    datosPersonaje.close()
    return listaCargada

def cargarBaseModificable():
    listaListas=[]
    baseMod = open("baseModificable.txt","rb")
    listaObj=pickle.load(baseMod)
    for objeto in listaObj:
        listaListas.append([objeto.obtenerNombre(),objeto.obtenerTuplaMedida(),objeto.obtenerListaTipos(),
                            objeto.obtenerEsShiny(),objeto.obtenerImagen()])
    baseMod.close()
    return listaListas

def grabarBaseModificable(listaCapturados):
    baseMod = open("baseModificable.txt","wb")
    pickle.dump(listaCapturados,baseMod)
    baseMod.close()
    return ""

def agregarCapturado(tuplaPokemon):
    listaTipos=[]
    sumaStats=0
    infoPoke=pb.pokemon(tuplaPokemon[0])
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
    if tuplaPokemon[-1]:
        puntos*=10
    pokeActual=(tuplaPokemon[0],(infoPoke.height*10,infoPoke.weight*10),listaTipos,puntos)
    pokemonAtr = Pokemon()
    pokemonAtr.asignarNombre(pokeActual[0])
    pokemonAtr.asignarTuplaMedidas(pokeActual[1])
    pokemonAtr.asignarListaTipos(pokeActual[2])
    pokemonAtr.asignarPuntos(pokeActual[3])
    pokemonAtr.asignarEsShiny(tuplaPokemon[-1])
    sprite=pb.pokemon(pokeActual[0]).sprites
    if tuplaPokemon[-1]:
        pokemonAtr.asignarImagen(sprite.front_shiny)
    else:
        pokemonAtr.asignarImagen(sprite.front_default)
    listaCapturados=cargarBaseModificable()
    listaCapturados.append(pokeActual)
    grabarBaseModificable(listaCapturados)
    return ""

def obtenerImagen(nombrePoke,esShiny):
    sprite=pb.pokemon(nombrePoke).sprites
    if esShiny:
        return ImageTk.PhotoImage(Image.open(BytesIO(requests.get(sprite.front_shiny).content)))
    else:
        return ImageTk.PhotoImage(Image.open(BytesIO(requests.get(sprite.front_default).content)))
                            
def encontrarPokemon(): # diccPokemon[pokemon]=(pokemon,(infoPoke.height*10,infoPoke.weight*10),listaTipos,puntos)
    baseEstatica=open("baseEstatica.txt","rb")
    diccPokes=pickle.load(baseEstatica)
    numPokemon = random.randint(1,len(diccPokes))
    if random.randint(1,2)==1:
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
    -index(int): Indica la pokeball que fue seleccionada.
    -baya(bool): True si el pokémon ha consumido una baya, False en caso contrario.
    Salida:
    -(bool): Determina si el pokemon se atrapará.
    """
    captura = False
    if index == 1 or index == 2 or index == 3:
        ratioCaptura=index
    else:
        ratioCaptura=20
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
    if random.randint(1,100)<=ratioCaptura:
        return True
    else:
        return False
    #Los puntos son directamente proporcionales al ratio de captura. Si da 300pts, el ratio de
    #captura es de 75, si da 600 es de 50, si da 900 es de 25, y si da 1800 puntos es de 5.
    #La Pokéball multiplica el ratio de captura por 1, la superball por 2, la ultraball por 3, y la
    #masterball por 20.
    #Se genera un número aleatorio de manera que la posibilidad de captura sea acorde a los
    #ratios dados

def enviarCorreo(nombrePokemon,pts):
    correo=EmailMessage()
    correo.set_content("¡Mira! He atrapado este "+nombrePokemon+" y me dio "+str(pts)+" puntos.")
    correo['Subject'] = "¡He capturado algo! :D"
    correo["From"]="soggycat64@gmail.com"
    correo["To"]="soggycat64@gmail.com"
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    server.set_debuglevel(1)
    server.login("soggycat64@gmail.com", "afhd rgun lrmy drcv")
    server.send_message(correo)
    server.quit()
    return messagebox.showinfo(title="¡Compartido!",message="Se ha enviado un correo")

def comprarItem(listaJugador,index):
    if index==1:
        if listaJugador[0]<100:
            messagebox.showwarning(title="Falta de brete",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-100
    elif index==2 or index==5:
        if listaJugador[0]<300:
            messagebox.showwarning(title="Falta de brete",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-300
    elif index==3:
        if listaJugador[0]<900:
            messagebox.showwarning(title="Falta de brete",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-900
    else:
        if listaJugador[0]<18000:
            messagebox.showwarning(title="Falta de brete",message="No tienes suficientes puntos.")
            return listaJugador
        listaJugador[0]=listaJugador[0]-18000 
    listaJugador[index]=listaJugador[index]+1
    grabarPersonaje(listaJugador)
    return listaJugador
    
def obtenerPokes():
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

