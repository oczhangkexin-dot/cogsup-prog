from expyriment import design, control, stimuli
import math
control.set_develop_mode(False)
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Edges", background_colour=(100, 100, 100))

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#Create a kanizsa-square
ks = stimuli.Rectangle(size=(270,270), colour=(100,100,100))

#Create 4 circles
cls = []
for i in range(4):
    c=i
    i = stimuli.Circle(radius=54, position=(135 * math.sqrt(2) * math.cos(-math.pi/4 + math.pi*c/2),  135 * math.sqrt(2) * math.sin(-math.pi/4 + math.pi*c/2)), colour='white')
    cls.append(i)

#Present the square and circles
for i in cls:
    if cls.index(i) == 0:
        i.present(clear=True, update=False)
    else:
        i.present(clear=False, update=False)

ks.present(clear=False, update=True)

# Leave them on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()