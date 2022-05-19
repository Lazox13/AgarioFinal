import core
import random
import pygame
from pygame import Vector2

class Joueur():
    def __init__(self):
        self.Position = Vector2(random.randint(0, 800), random.randint(0, 800))
        self.Couleur = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
        self.Rayon = 10
        self.RayonMax = 150

        self.Raideur = 0.035
        self.Vitesse = 1
        self.VitesseMax = 5
        self.Direction = Vector2()
        self.Ux = Vector2()
        self.l = 0
        self.l0 = 10
        self.L = 0
        self.Fx = 0

    def dessiner(self):
        pygame.draw.circle(core.screen, self.Couleur, self.Position, self.Rayon)

    def deplacer(self, clic):

        if self.Position.y < 0 or self.Position.y > core.WINDOW_SIZE[0]:
            self.Direction = Vector2(self.Direction.x, self.Direction.y * -1)

        if self.Position.x < 0 or self.Position.x > core.WINDOW_SIZE[1]:
            self.Direction = Vector2(self.Direction.x * -1, self.Direction.y)

        if clic is not None:

            self.Ux = clic - self.Position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.Raideur * self.L * self.Ux
            self.Direction = self.Direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)


        if self.Direction.length() > self.VitesseMax and self.Direction.length() !=0 :
            self.Direction.normalize()
            self.Direction.scale_to_length(self.VitesseMax)

        self.Position = self.Direction + self.Position

    def grossir(self):
        if self.Rayon < 150:
            self.Rayon = self.Rayon + 1

            self.VitesseMax = self.VitesseMax * 0.988
            self.Fx = self.Vitesse * self.Fx

    def mourir(self):
        self.Position = Vector2(random.randint(0, 800), random.randint(0, 800))
        self.Rayon = 10