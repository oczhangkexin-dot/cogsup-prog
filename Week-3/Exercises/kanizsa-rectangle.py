from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
import math
control.set_develop_mode(False)
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Edges", background_colour=C_GREY)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#Create a kanizsa-square
ks = stimuli.Rectangle(size=(270,270), colour=C_GREY)



def stim(rec_ratio, scale_rec, scale_circle):
    screen_w = 1080
    
    #Create a rectangle 
    rec_w = screen_w // scale_rec
    rec_h = rec_w // rec_ratio
    ks = stimuli.Rectangle(size=(rec_w, rec_h), colour=C_GREY)
    
    #Create 4 circles
    pos = []
    for m in [rec_w/2, -rec_w/2]:
        for n in [rec_h/2, -rec_h/2]:
            pos.append((m, n))

    cls = []
    for i in range(4):
        c=i
        i = stimuli.Circle(radius=screen_w // scale_circle, position=pos[c], colour='white')
        cls.append(i)
    
    return cls + [ks]

stimu = stim(0.75, 5, 20)

#Present the square and circles
exp.screen.clear()
for i in stimu:
    if stimu.index(i) < len(stimu) - 1:
        i.present(clear=False, update=False)
    else:
        i.present(clear=False, update=True)

# Leave them on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()