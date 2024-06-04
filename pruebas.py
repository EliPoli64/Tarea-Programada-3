import pokebase as pb
from tkinter import *
from clases import *
import playsound
import webbrowser
import pokebase as pb
import pickle
import playsound
import random
from tkinter import Image
from PIL import ImageTk
from PIL import Image
import requests
from io import BytesIO

from tkinter import *

from tkinter import Tk, Canvas, NW
from PIL import ImageTk



t = Tk()
t.title("Transparency")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="Leopard-Download-PNG.png")
canvas.create_image(0,1920, image=photoimage)

t.mainloop()