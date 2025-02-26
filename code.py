# SPDX-FileCopyrightText: 2025 Jacques Supcik <jacques.supcik@hefr.ch>
#
# SPDX-License-Identifier: Apache-2.0 OR MIT

"""
Spirograph
"""

from math import cos, radians, sin

import board
from adafruit_turtle import Color, turtle

GRAND_RAYON = 150
PETIT_RAYON = 65
RAYON_STYLO = 24
CHANGEMENT_CRAYON = 200


class Spinograph:

    def __init__(self, turtle):
        self.turtle = turtle
        # Dessine le grand cercle
        self.turtle.pencolor(Color.GRAY)
        self.turtle.penup()
        self.turtle.goto(0, -GRAND_RAYON)
        self.turtle.pendown()
        self.turtle.circle(GRAND_RAYON)
        self.turtle.penup()

    def goto(self, angle):
        # Calcule la position du centre du petit cercle
        x0 = (GRAND_RAYON - PETIT_RAYON) * sin(angle)
        y0 = (GRAND_RAYON - PETIT_RAYON) * cos(angle)
        # Calcule l'angle de rtation du petit cercle
        beta = angle * GRAND_RAYON / PETIT_RAYON
        # Calcule la position du stylo
        x = x0 - RAYON_STYLO * sin(angle - beta)
        y = y0 - RAYON_STYLO * cos(angle - beta)
        self.turtle.goto(x, y)


colors = [
    Color.BLUE,
    Color.BROWN,
    Color.GREEN,
    Color.LIGHT_GRAY,
    Color.ORANGE,
    Color.PINK,
    Color.PURPLE,
    Color.RED,
    Color.TURQUOISE,
    Color.YELLOW,
]

turtle = turtle(board.DISPLAY)
s = Spinograph(turtle)
s.goto(0)
turtle.pendown()

i = 0
while True:
    i += 1
    turtle.pencolor(colors[int(i / CHANGEMENT_CRAYON) % len(colors)])
    s.goto(radians(i))
