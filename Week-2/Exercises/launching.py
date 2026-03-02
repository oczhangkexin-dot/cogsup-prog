# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two Rectangles")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

rec1 = stimuli.Rectangle(size=(50, 70), colour='red', position=(-375, 0))

rec2 = stimuli.Rectangle(size=(50, 70), colour='green', position=(25, 0))
            
rec1.present(clear=True, update=False)

rec2.present(clear=False, update=True)

i = 0
while i < 280:
    rec1.move(offset=(1.25, 0))
    rec1.present(clear=True, update=False)
    rec2.present(clear=False, update=True)
    i+=1

i = 0
while i < 280:
    rec2.move(offset=(1.25, 0))
    rec1.present(clear=True, update=False)
    rec2.present(clear=False, update=True)
    i+=1

# Leave the fixation on-screen for 500 ms
exp.clock.wait(1000)


# End the current session and quit expyriment
control.end()
