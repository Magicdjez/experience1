from psychopy import visual
import numpy as np

class frame:

    def __init__(self, win):

        self.hauteur = 250 # hauteur du cadre/2
        self.largeur = 250 # largeur du cadre/2
        self.couleur_frame = [0, 0, 0] # couleur des extrémités
        self.epaisseur_frame = 2 # épaisseur de la barre en pixels

        # crée la liste des textures des parties fixes du "scroll bar"

        self.frame = []

        self.frame.append(
            visual.Line(
                win,
                start=(-self.largeur, -self.largeur),
                end=(-self.hauteur, self.largeur),
                lineWidth=self.epaisseur_frame,
                lineColor=self.couleur_frame,
                colorSpace='rgb1'
            )
        ) # crée une texture pour la ligne a gauche

        self.frame.append(
            visual.Line(
                win,
                start=(-self.largeur, self.largeur),
                end=(self.hauteur, self.largeur),
                lineWidth=self.epaisseur_frame,
                lineColor=self.couleur_frame,
                colorSpace='rgb1'
            )
        ) # crée une texture pour la ligne du haut

        self.frame.append(
            visual.Line(
                win,
                start=(self.largeur, -self.largeur),
                end=(self.hauteur, self.largeur),
                lineWidth=self.epaisseur_frame,
                lineColor=self.couleur_frame,
                colorSpace='rgb1'
            )
        ) # crée une texture pour la ligne de droite

        self.frame.append(
            visual.Line(
                win,
                start=(-self.largeur, -self.hauteur),
                end=(self.hauteur, -self.hauteur),
                lineWidth=self.epaisseur_frame,
                lineColor=self.couleur_frame,
                colorSpace='rgb1'
            )
        ) # crée une texture pour la ligne du bas

    def draw(self):
        for item in self.frame:
            item.draw()

        return self