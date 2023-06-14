from tkinter import *
from tkinter import colorchooser


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicație de Desen")
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.draw_color = "white"
        self.drawing = False

        self.clear_button = Button(self.root, text="Șterge", command=self.clear_drawing)
        self.clear_button.pack()

        self.color_button = Button(self.root, text="Selectează Culoare", command=self.select_color)
        self.color_button.pack()

    def start_drawing(self, event):
        self.drawing = True
        self.prev_x = event.x
        self.prev_y = event.y

    def draw(self, event):
        if self.drawing:
            self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill=self.draw_color)
            self.prev_x = event.x
            self.prev_y = event.y

    def stop_drawing(self, event):
        self.drawing = False

    def clear_drawing(self):
        self.canvas.delete("all")

    def select_color(self):
        color = colorchooser.askcolor(initialcolor=self.draw_color)[1]
        if color:
            self.draw_color = color


root = Tk()
app = DrawingApp(root)
root.mainloop()