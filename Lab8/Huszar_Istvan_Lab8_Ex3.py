from tkinter import *


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.selected_shape = None
        self.start_x = None
        self.start_y = None

        self.shapes = []

        self.create_menu()
        self.canvas.bind("<Button-1>", self.handle_left_click)
        self.canvas.bind("<B1-Motion>", self.handle_left_drag)
        self.canvas.bind("<ButtonRelease-1>", self.handle_left_release)
        self.canvas.bind("<Button-3>", self.handle_right_click)
        self.canvas.bind("<Double-Button-1>", self.handle_double_click)

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        shape_menu = Menu(menu)
        menu.add_cascade(label="Shapes", menu=shape_menu)
        shape_menu.add_command(label="Oval", command=self.select_oval)
        shape_menu.add_command(label="Polygon", command=self.select_polygon)
        shape_menu.add_command(label="Line", command=self.select_line)
        shape_menu.add_command(label="Arc", command=self.select_arc)

        menu.add_command(label="Clear All", command=self.clear_all)

    def select_oval(self):
        self.selected_shape = "oval"

    def select_polygon(self):
        self.selected_shape = "polygon"

    def select_line(self):
        self.selected_shape = "line"

    def select_arc(self):
        self.selected_shape = "arc"

    def handle_left_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def handle_left_drag(self, event):
        if self.selected_shape:
            self.draw_shape(event)

    def handle_left_release(self, event):
        if self.selected_shape:
            self.draw_shape(event)
            self.selected_shape = None

    def draw_shape(self, event):
        x = min(self.start_x, event.x)
        y = min(self.start_y, event.y)
        width = abs(event.x - self.start_x)
        height = abs(event.y - self.start_y)

        if self.selected_shape == "oval":
            shape = self.canvas.create_oval(x, y, x + width, y + height)
        elif self.selected_shape == "polygon":
            shape = self.canvas.create_polygon(x, y, x + width, y, x + width, y + height, x, y + height)
        elif self.selected_shape == "line":
            shape = self.canvas.create_line(x, y, event.x, event.y)
        elif self.selected_shape == "arc":
            shape = self.canvas.create_arc(x, y, x + width, y + height, start=0, extent=180)

        self.shapes.append(shape)

    def handle_right_click(self, event):
        if self.shapes:
            last_shape = self.shapes[-1]
            x = event.x - self.canvas.coords(last_shape)[0]
            y = event.y - self.canvas.coords(last_shape)[1]
            self.canvas.move(last_shape, x, y)

    def handle_double_click(self, event):
        for shape in self.shapes:
            self.canvas.delete(shape)
        self.shapes = []

    def clear_all(self):
        for shape in self.shapes:
            self.canvas.delete(shape)
        self.shapes = []


root = Tk()
app = DrawingApp(root)
root.mainloop()