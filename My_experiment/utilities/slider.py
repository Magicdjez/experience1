from psychopy import visual
import numpy as np

class slider:

    def __init__(self, win):

        self.demie_extremite = 10 # hauteur de la moitié des extrémités de la bar en pixels
        self.epaisseur_extremite = 2 # épaisseur de la barre en pixels
        self.couleur_extremite = [0, 0, 0] # couleur des extrémités
        self.demie_barre = 400 # longueur de la moitié de la barre en pixels
        self.epaisseur_barre = 2 # épaisseur de la barre en pixels 
        self.couleur_barre = [0, 0, 0] # couleur de la barre
        self.demie_marque = 5 # hauteurr de la moitié d'une marque 
        self.epaisseur_marque = 1 # épaisseur des marques
        self.couleur_marque = [0, 0, 0] # couleur des marques
        self.nb_marques = 10 # nombre de marques incluant les extrémités
        self.position_y = 0 # position de la barre sur l'axe des y en pixels
        self.texte_gauche = '0' # texte à gauche de la barre
        self.texte_droite = '100' # texte à droite de la barre
        self.taille_texte = 12 # taille du texte
        self.police_texte = 'Helvetica' # police de caractère
        self.couleur_texte = [0, 0, 0] # couleur texte
        self.hauteur_texte = 8  # position du texte par rapport aux extrémités

        # crée la liste des textures des parties fixes du "scroll bar"

        self.scroll_bar_fixe = []

        self.scroll_bar_fixe.append(
            visual.Line(
                win,
                start=(-self.demie_barre, self.position_y),
                end=(self.demie_barre, self.position_y),
                lineWidth=self.epaisseur_barre,
                lineColor=self.couleur_barre,
                colorSpace='rgb1'
            )
        ) # crée une texture pour la barre du "scroll bar"

        for ii in np.linspace(
            -self.demie_barre,
            self.demie_barre,
            self.nb_marques):
            self.scroll_bar_fixe.append(
                visual.Line(
                    win,
                    start=(ii, self.position_y-self.demie_marque),
                    end=(ii, self.position_y+self.demie_marque),
                    lineWidth=self.epaisseur_marque,
                    lineColor=self.couleur_marque,
                    colorSpace='rgb1'
                )
            ) # crée des textures pour les marques du "scroll bar"

        self.scroll_bar_fixe.append(
            visual.Line(
                win,
                start=(-self.demie_barre, self.position_y-self.demie_extremite),
                end=(-self.demie_barre, self.position_y+self.demie_extremite),
                lineWidth=self.epaisseur_extremite, lineColor=self.couleur_extremite,
                colorSpace='rgb1'
            )
        ) # crée des texture pour l'extrémité gacuhe du "scroll bar"

        self.scroll_bar_fixe.append(
            visual.Line(
                win,
                start=(self.demie_barre, self.position_y-self.demie_extremite),
                end=(self.demie_barre, self.position_y+self.demie_extremite),
                lineWidth=self.epaisseur_extremite,
                lineColor=self.couleur_extremite,
                colorSpace='rgb1'
            )
        ) # crée des texture pour l'extrémité droite du "scroll bar"

        self.scroll_bar_fixe.append(
            visual.TextStim(
                win,
                text=self.texte_gauche,
                color=self.couleur_texte,
                height=self.taille_texte,
                font=self.police_texte,
                pos=[-self.demie_barre, self.position_y+self.demie_extremite+self.hauteur_texte],
                colorSpace='rgb1'
            )
        ) # crée texture du texte à gauche de la barre

        self.scroll_bar_fixe.append(
            visual.TextStim(
                win,
                text=self.texte_droite,
                color=self.couleur_texte,
                height=self.taille_texte,
                font=self.police_texte,
                pos=[self.demie_barre, self.position_y+self.demie_extremite+self.hauteur_texte],
                colorSpace='rgb1'
            )
        ) # crée texture du texte à droite de la barre

    def draw(self):
        for item in self.scroll_bar_fixe:
            item.draw()

        return self





# pclick = False

# start_time = core.Clock()
# ms = pve.Mouse(
#     win=win
#     )

# while not pclick:
#     # define line that moves
#     ms.clickReset()
#     scale_line = pv.Line(
#         win=win,
#         units='pix',
#         lineColor='white',
#         lineWidth=10
#     )

#     curpos = ms.getPos()
#     win = scale_view(win)
#     if curpos[0] > -603 and curpos[0] < 603:
#         scale_line.start = [curpos[0], -20]
#         scale_line.end = [curpos[0], 0]
#         scale_line.draw()
#         win.flip()
#         buttons, times = ms.getPressed(getTime=True)
#         if buttons[0] == 1:
#             pclick=True
#             win.flip()
#     else:
#         win.flip()

#     if pve.getKeys(keyList=['escape','q']):
#         core.quit()

# wait for keys at the end.
# pve.waitKeys()

# win.close()