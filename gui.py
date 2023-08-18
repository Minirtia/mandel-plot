import tkinter as tk
from tkinter import ttk
from mandel_plot import MandelPlotter, DEFAULT_PLOTTER
from PIL import Image, ImageTk

class Window:
    def __init__(self, image):
        self.image = image
        self.root = tk.Tk()
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        self.img = tk.PhotoImage(file=self.image)
        label = tk.Label(self.root, image = self.image)
        label.pack

def main():
    DEFAULT_PLOTTER.make_picture()
    DEFAULT_PLOTTER.save_image()

    Window('/home/calebmay/mandel-plot/output.png')

    


if __name__ == "__main__": 
    main()
