from psychopy import event, core 

def quit_func(win):
    """ Checks whether the exit key 'q' has been pressed. If so, closes window and quits experiment.
    Args:
        win (psychopy.visual.window.Window): window where the experiment is displayed
    """
    if event.getKeys(keyList=['q']):
        win.close()
        core.quit()
        