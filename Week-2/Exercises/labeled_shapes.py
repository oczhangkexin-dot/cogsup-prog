import math
# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Shapes2")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#Create a triangle
tri = stimuli.Shape(colour='purple', position=(-100, 0))
tri.add_vertices([(50,0), (-25,25*math.sqrt(3))])


#Create a hexagon
hex = stimuli.Shape(colour='yellow', position=(100, 0))
hex.add_vertices([(12.5, -12.5*math.sqrt(3)), (25, 0), (12.5, 12.5*math.sqrt(3)), (-12.5, 12.5*math.sqrt(3)), (-25, 0)])
            
#Create lines
l1 = stimuli.Shape(colour='white', position=(-100, 25*math.sqrt(3)+5))
l1.add_vertices([(3,0), (0,50), (-3,0)])
l2 = stimuli.Shape(colour='white', position=(100, 25*math.sqrt(3)+5))
l2.add_vertices([(3,0), (0,50), (-3,0)])

#Create textboxes
txt1 = stimuli.TextBox('triangle', size=(80, 30), position=(-100, 25*math.sqrt(3)+50), text_colour='white')
txt2 = stimuli.TextBox('hexagon', size=(80, 30), position=(100, 25*math.sqrt(3)+50), text_colour='white')

#Present the stimuli
tri.present(clear=True, update=False)
l1.present(clear=False, update=False)
txt1.present(clear=False, update=False)
hex.present(clear=False, update=False)
l2.present(clear=False, update=False)
txt2.present(clear=False, update=True)

# Leave the on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
