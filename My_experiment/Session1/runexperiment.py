import sys
import numpy as np
from psychopy import visual, logging, event, monitors, core 
import os
import serial
from task_proto import task
from task_proto import run_experiment

fullScreen = True # True = full screen, False = not full screen
eeg = False       # True = using eeg, need triggers
ordi_labo = True

subject = str(sys.argv[1]) # participant ID

# third argument is session ??
session = int(sys.argv[3])

"""
STIMULI (change for different subjects) :  girafe, soulier noir, fruit, bus
"""
image_path = os.path.join(
    os.path.expanduser('~'),
    'projects',
    'mentalimagery',
    'mentalimagery',
    'Images' 
)

images_stim = ["Bus_jaune.png", "Giraffe.png"]
"""
INITIALIZATION
"""
 # folder to contain results
res_path = os.path.join(
    os.path.expanduser('~'),
    'projects',
    'My_experiment',
    'Session1',
    'results'
)
results_dir = os.path.join(res_path, f'{subject}')

# when ready for the real task, remove the first line so that 
# throws FileExistsError when the file already exists 
if not os.path.exists(results_dir): 
    os.makedirs(results_dir)

# initiate parameters dict
params = {}
params['session'] = session

"""
MONITOR: uncomment if using a monitor
"""
mon_name = monitors.getAllMonitors()[0]
mon = monitors.Monitor(mon_name)
mon.setDistance(70)
#mon = monitors.Monitor('LenovoThinkPadP1', width=43.9, distance=60.)
mon.setSizePix((1920, 1080))
mon.save()

""" 
EEG port
"""
if eeg==True:
    #port = serial.Serial('/dev/ttyUSB0', 115200) # adjust with right port and baudrate
    port = serial.Serial('/dev/ttyUSB0', 115200) #??
    #port.timeout = 1
    #port.flush()
"""
WINDOW
"""
if ordi_labo == True:
    win_size = [2540, 1440]
else:
    win_size = [1920, 1080]

if fullScreen:
    win = visual.Window(size = win_size,units='pix', monitor = mon, fullscr=True, color=[0.5, 0.5, 0.5], colorSpace = 'rgb1')
else :
    win = visual.Window(size = win_size, units='pix', monitor=mon, fullscr=False, color=[0.5, 0.5, 0.5], colorSpace = 'rgb1')

    params['session'] = session          # Session number
    params['n_trials'] = 300             # Second image presentation time
    params['images_stim'] = images_stim  
    params['results_dir'] = results_dir
    # Time delays
    params['fixation_time'] = 0.5
    params['first_im_time'] = 3
    params['second_im_time'] = 3
    params['instruct_time'] = 1          # Instructions presentation time 
    params['imagery_time'] = 3           # Imagery time 
    # "scroll bar" mobile part
    params['epaisseur_ligne'] = 3        # Width
    params['couleur_ligne'] = [1, 0, 0]  # Color
    # EEG 
    params['eeg'] = eeg                # True if using eeg, False otherwise 

    params['port'] = port if eeg == True else None      
experience= run_experiment.Experiment(win, params, results_dir, subject, session, eeg, port)