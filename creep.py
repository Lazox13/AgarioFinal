import core
import random
import pygame
from pygame.math import Vector2

class Creep:
    def __init__(self):
        self.Position = Vector2(random.randint(0, 800), random.randint(0, 800))
        self.Rayon = 5
        self.Couleur = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        self.Masse = 10


    def dessiner(self):
        pygame.draw.circle(core.screen, self.Couleur, self.Position, self.Rayon)

    def mourir(self):
        self.Position = Vector2(random.randint(0, 800), random.randint(0, 800))
