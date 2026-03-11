# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two Rectangles")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

rec1 = stimuli.Rectangle(size=(50, 50), colour='red', position=(-100, 0))

rec2 = stimuli.Rectangle(size=(50, 50), colour='green', position=(100, 0))
            
rec1.present(clear=True, update=False)

rec2.present(clear=False, update=True)

# Leave the on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
