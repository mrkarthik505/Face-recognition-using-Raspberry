from Tkinter import *
import Tkinter as tk
import PIL
import webbrowser
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
from PIL import Image, ImageTk, ImageSequence
from sampleGIF_bb_py2 import App
from CloudWidgets_workingmainpage_py2 import widget_page

root = tk.Tk()
App = App(root)
root.mainloop()

we = widget_page()

