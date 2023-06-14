import pygame
import random


pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circles")
RED = (255, 0, 0)
BLUE = (0, 0, 255)
circles = []

for i in range(20):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(10, 15)
    circles.append({"x": x, "y": y, "radius": radius, "color": RED})

running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:
                # check if the mouse click is inside a circle
                pos = pygame.mouse.get_pos()
                for circle in circles:
                    distance = ((pos[0] - circle["x"])**2 + (pos[1] - circle["y"])**2)**0.5
                    if distance <= circle["radius"]:
                        if circle["color"] == RED:
                            circle["color"] = BLUE
                        else:
                            circle["color"] = RED

    screen.fill((255, 255, 255))
    for circle in circles:
        pygame.draw.circle(screen, circle["color"], (circle["x"], circle["y"]), circle["radius"])
    pygame.display.update()
pygame.quit()
