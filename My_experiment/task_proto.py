import os
from psychopy import core, visual, event
from ..utilities import (FixationCross, slider, frame)
from ..utilities.quit_func import quit_func 
import numpy as np
import random

class  task():
    # Initialize the task
    def __init__(self, subject, win, params, logging):
        self.win = win                                   # Window
        self.session = params['session']                 # Session number    
        self.n_trials = params['n_trials']               # Number of trials         
        self.images_stim = params['images_stim']         # Images used as stimuli in array format 
        self.results_dir = params['results_dir']         # Path to results file
    # Time delays
        self.fixation_time = params['fixation_time']     # Fixation cross time
        self.first_im_time = params['im_time']             # image presentation time 
        self.instruct_time = params['instruct_time']     # Instructions presentation time 
        self.imagery_time = params['imagery_time']       # Imagery time 
        # "Scroll bar" mobile part
        self.epaisseur_ligne = params['epaisseur_ligne'] # Width
        self.couleur_ligne = params['couleur_ligne']     # Color
     # EEG
        self.eeg = params['eeg']                         # True if using eeg
        self.port = params['port']                       # Serial port
        self.textures = []
        for image in self.images_stim:
            self.textures.append(visual.ImageStim(win, image=image, size=(np.shape(image)[0], np.shape(image)[0]), colorSpace='rgb1'))

        self.results = {}                                                                 # Dictionary to contain the results
        self.results_file = os.path.join(self.results_dir, f'{subject}_imagery_{self.session}.npy') # Name of the results file
        
        self.results['refresh_rate'] = self.win.getActualFrameRate() # Window's refresh rate (Hz)
        self.results['window_size'] = self.win.size         
        self.fix = FixationCross(win)         # Window's dimensions (pixels)
        self.framer = frame(win)      # Create frame to delimit imagery area
        self.slide = slider(win)      # Create slider 

        self.onsets_t_current_trial = {}

    def cros(self):
        ''' Show fixation cross '''
        if self.eeg==True:
            trigger = int(str(7))
            self.win.callOnFlip(self.onEvent, self.port, trigger)
            self.win.timeOnFlip(self.onsets_t_current_trial, 'onset_fix1')
        self.fix.draw()
        self.win.flip()
        quit_func(self.win)  # Exit experiment if 'q' key is pressed 
        core.wait(self.fixation_time)

    def onEvent(self, t:int):
        self.port.write(bytes([t]))

    def show_image(self,indice):
        ''' Show image '''
        if self.eeg==True:
            trigger = int(str(indice))
            self.win.callOnFlip(self.onEvent, self.port, trigger)
            self.win.timeOnFlip(self.onsets_t_current_trial, 'onset_im'+"str(indice)")
        self.textures[indice].draw()
        self.win.flip()
        quit_func(self.win)
        core.wait(self.imagery_time)


    def show_text(self, text):
        ''' Show text'''
        if self.eeg==True:
            trigger = int(str(10))
            self.win.callOnFlip(self.onEvent, self.port, trigger)
            self.win.timeOnFlip(self.onsets_t_current_trial, 'onset_text')
        text.draw()
        self.win.flip()
        quit_func(self.win)
        core.wait(self.instruct_time)

    
    def welcome_screen(self):
        ''' Show welcome screen '''
        welcome = visual.TextStim(self.win, text='Bienvenue !', color='black', height=0.1)
        self.show_text(welcome)
        core.wait(self.instruct_time)

    def condifent_slide(self): # à tester!!!
        confSlider = visual.Slider(win=self.win, pos=[0, -0.4], ticks=[1, 50, 100],
                           size=[1.0, 0.1], labels=['Pas confiant', '', 'Très confiant'], 
                           granularity=1, showValue=True)
        while True:
        # Affichage de la barre de confiance
            confSlider.draw()
            self.win.flip()
    
    # Attendre la réponse de l'utilisateur
            allKeys = event.waitKeys()
    
    # Si l'utilisateur appuie sur la touche "ESCAPE", on arrête l'expérience
            if 'escape' in allKeys:
                break
    
    # Si l'utilisateur déplace le curseur, on enregistre sa réponse
            if confSlider.getRating() is not None:
                confResponse = confSlider.getRating()
                print("Confiance du participant : ", confResponse)
                break
        
    def exit(self):
        ''' Exit experiment '''
        self.win.close()
        core.quit()


def run_experiment(subject, win, params, logging,Ntrial):
    experiment=task(subject, win, params, logging)
    experiment.welcome_screen()
    experiment.show_text(" concentrez vous sur les images")
    experiment.cros()
    for i in range(Ntrial):
        for i in range(len(experiment.images_stim)):
            experiment.show_image(i)
            experiment.show_text("concentrez vous sur les images")
            experiment.cros()
        chiffre_aleatoire = random.randint(1, 2)
        experiment.show_text("imaginer l'image"+str(chiffre_aleatoire))
        core.wait(3)
        experiment.show_text("note la precision de votre imagination")
        experiment.condifent_slide()
    experiment.show_text("fin de l'experience, merci de votre participation")
    core.wait(3)
    experiment.exit()


def stimloader(path='Images'):
    """helper function for loading stimuli

    Args:
        path (str, optional): path to images directory.
                              Defaults to 'Images'.

    Returns:
        Images (np.ndarray): images as an array of shape:
                             x, y, rgb, n_images.
    """

    files = glob(os.path.join(path, '*.png'))
    files.sort()

    # print(files)

    images = []
    for file in files:
        img = np.flip(np.array(Image.open(file), order="C"), axis=0).astype(np.float32)

        if img.max() > 1:
            img *= 1.0/255.0
        images.append(img)

    return images


 
