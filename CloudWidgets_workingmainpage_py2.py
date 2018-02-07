from Tkinter import *
import Tkinter as tk
import PIL
import webbrowser
from PIL import Image,ImageTk
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

class widget_page:
    def __init__(self):    
        win = tk.Tk()
        win.title("Cloud Window")
        win.configure(background='black')
        win.minsize(width=1024, height=512)


        def FBLINK(event):
                webbrowser.open_new("http://www.facebook.com")

        def TWLINK(event):
                webbrowser.open_new("http://www.twitter.com")

        def YULINK(event):
                webbrowser.open_new("http://www.youtube.com")

        def MVLINK(event):
                webbrowser.open_new("http://www.movie.com")
                
        def SOLINK(event):
                webbrowser.open_new("http://www.song.com")
                
        def IMLINK(event):
                webbrowser.open_new("http://www.image.com")
                
        def MPLINK(event):
                webbrowser.open_new("http://www.map.com")
                
        def GALINK(event):
                webbrowser.open_new("http://www.games.com")

        imgFB = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/facebook2.png"))
        panel = tk.Label(win, image = imgFB, cursor="hand2",background='black')
        panel.bind("<1>", FBLINK)
        panel.grid(row=1,column=1)

        imgTW = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/twitter.png"))
        panel = tk.Label(win, image = imgTW, cursor="hand2",background='black')
        panel.bind("<1>", TWLINK)
        panel.grid(row=2,column=1)

        imgYU = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/youtube.png"))
        panel = tk.Label(win, image = imgYU, cursor="hand2",background='black')
        panel.bind("<1>", YULINK)
        panel.grid(row=1,column=2)

        imgMV = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/Movies.png"))
        panel = tk.Label(win, image = imgMV, cursor="hand2",background='black')
        panel.bind("<1>", MVLINK)
        panel.grid(row=2,column=2)

        imgSO = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/Music.png"))
        panel = tk.Label(win, image = imgSO, cursor="hand2",background='black')
        panel.bind("<1>", SOLINK)
        panel.grid(row=1,column=3)

        imgIM = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/Images.png"))
        panel = tk.Label(win, image = imgIM, cursor="hand2",background='black')
        panel.bind("<1>", IMLINK)
        panel.grid(row=2,column=3)

        imgMP = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/Map.png"))
        panel = tk.Label(win, image = imgMP, cursor="hand2",background='black')
        panel.bind("<1>", MPLINK)
        panel.grid(row=1,column=4)

        imgGA = ImageTk.PhotoImage(Image.open("Pictures/3D Icons/Games.png"))
        panel = tk.Label(win, image = imgGA, cursor="hand2",background='black')
        panel.bind("<1>", GALINK)
        panel.grid(row=2,column=4)

        tk.mainloop()
