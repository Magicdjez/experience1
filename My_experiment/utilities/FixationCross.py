from psychopy import visual

class FixationCross:
    # Creates a fixation in the center of the window
    
    def __init__(self, win, start=[[-10, 0],[0, -10]], end=[[10, 0],[0, 10]], thickness=1, color=[1, 0, 0]):

        self.horizontal = visual.Line(win, start=start[0], end=end[0], lineWidth=thickness, lineColor=color, colorSpace='rgb1')
        self.vertical = visual.Line(win, start=start[1], end=end[1], lineWidth=thickness, lineColor=color, colorSpace='rgb1')
    def draw(self):
        self.horizontal.draw()
        self.vertical.draw()