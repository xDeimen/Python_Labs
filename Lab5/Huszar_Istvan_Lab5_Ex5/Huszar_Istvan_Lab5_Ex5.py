from graphics import *
import random

# Define the colors to be used in the game
colors = ["red", "white", "black", "yellow", "blue"]

# Define the size of the squares in the grid
square_size = 50

# Define the size of the grid
grid_size = 5

# Create the window
win = GraphWin("Game box", square_size * grid_size, square_size * grid_size)

# Create the grid of squares
squares = []
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        x1 = j * square_size
        y1 = i * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        square = Rectangle(Point(x1, y1), Point(x2, y2))
        square.setFill(random.choice(colors))
        square.draw(win)
        row.append(square)
    squares.append(row)

# Play the game
while True:
    # Get the mouse click
    click_point = win.getMouse()

    # Get the square that was clicked
    square = None
    for row in squares:
        for s in row:
            if s.getP1().getX() <= click_point.getX() <= s.getP2().getX() and s.getP1().getY() <= click_point.getY() <= s.getP2().getY():
                square = s
                break
        if square:
            break

    # If no square was clicked, skip the rest of the loop
    if not square:
        continue

    # Get the color of the square
    color = square.config["fill"]

    # Determine the new color of the square
    new_color = None
    if color == "black":
        new_color = random.choice(["white", "yellow", "blue", "red"])
    elif color == "white":
        new_color = "black"
    elif color == "blue":
        new_color = "red"
    elif color == "yellow":
        new_color = "blue"
    elif color == "red":
        new_color = "yellow"

    # Set the new color of the square
    square.setFill(new_color)

    # Check if the game has been won
    game_won = True
    for row in squares:
        for s in row:
            if s.config["fill"] != new_color:
                game_won = False
                break
        if not game_won:
            break

    # If the game has been won, display a message and break out of the loop
    if game_won:
        message = Text(Point(win.getWidth() / 2, win.getHeight() / 2), "Felicitari ai castigat!")
        message.draw(win)
        break

# Wait for a mouse click to close the window
win.getMouse()
win.close()
