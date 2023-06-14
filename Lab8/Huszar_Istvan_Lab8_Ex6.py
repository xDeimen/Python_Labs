from tkinter import *


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        x = event.x
        y = event.y
        self.canvas.create_oval(x, y, x + 5, y + 5, fill="black")  # Desenează un punct de mărime 5x5


root = Tk()
app = DrawingApp(root)
root.mainloop()