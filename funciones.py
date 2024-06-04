import pokebase as pb
import pickle
import playsound
import random
from PIL import ImageTk
from PIL import Image
import requests
from io import BytesIO

#Si un Pokémon atrapado tiene menos de 300 en total de estadísticas, da 300pts. Si está
#entre 300 y 400 ambos inclusive dan 600pts. Entre 400 y 599 da 900pts, y 600 o más da
#1800pts.

"""def tocarCancion():
    playsound.playsound() 
"""
def grabarBaseEstatica():
    diccPokes=obtenerPokes()
    baseEstatica=open("baseEstatica.txt","wb")
    pickle.dump(diccPokes,baseEstatica)
    baseEstatica.close()
    return diccPokes
    
def grabarBaseModificable():
    pass

def encontrarPokemon(): # diccPokemon[pokemon]=(pokemon,(infoPoke.height*10,infoPoke.weight*10),listaTipos,puntos)
    baseEstatica=open("baseEstatica.txt","rb")
    diccPokes=pickle.load(baseEstatica)
    numPokemon = random.randint(1,len(diccPokes))
    sprite=pb.pokemon(diccPokes[numPokemon][0]).sprites
    if random.randint(1,1) ==1:
        tuplaPokemon=(diccPokes[numPokemon][0],diccPokes[numPokemon][-1]*10,
                      ImageTk.PhotoImage(Image.open(BytesIO(requests.get(sprite.front_shiny).content))))
    else:
        tuplaPokemon=(diccPokes[numPokemon][0],diccPokes[numPokemon][-1],
                      ImageTk.PhotoImage(Image.open(BytesIO(requests.get(sprite.front_default).content)))) 
    baseEstatica.close()
    return tuplaPokemon

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


"""def determinarAtrapado(prob,pts):
    """