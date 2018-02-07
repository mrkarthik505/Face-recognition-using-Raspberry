import Tkinter
from PIL import Image, ImageTk, ImageSequence

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Tkinter.Canvas(parent, width=1024, height=512,background='black')
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                Image.open("Pictures/Catalyst_face.gif"))]
        self.image = self.canvas.create_image(512,256, image=self.sequence[0])
        self.animating = True
        self.animate(0)
        
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.parent.after(33, lambda:self.animate((counter+1) % len(self.sequence)))
        #print(counter)
        

