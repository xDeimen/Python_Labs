from tkinter import *


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicație de Desen")
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack(side=LEFT)

        self.canvas.bind("<Button-1>", lambda event: self.set_color("blue"))
        self.canvas.bind("<Button-3>", lambda event: self.set_color("pink"))
        self.canvas.bind("<B1-Motion>", self.draw)

        self.color = "blue"

        self.side_window = Toplevel(self.root)
        self.side_canvas = Canvas(self.side_window, width=100, height=400)
        self.side_canvas.pack()
        self.side_canvas.create_rectangle(0, 0, 100, 400, fill="blue")
        self.side_canvas.create_rectangle(0, 0, 100, 200, fill="pink")

    def set_color(self, color):
        self.color = color

    def draw(self, event):
        x = event.x
        y = event.y
        self.canvas.create_oval(x, y, x + 5, y + 5, fill=self.color)


root = Tk()
app = DrawingApp(root)
root.mainloop()