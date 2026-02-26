# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Rectangle")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create a 50px-radius circle
Rectangle = stimuli.Rectangle(size=(50, 50), colour='blue')

# Start running the experiment
control.start(subject_id=1)

# Present the rectangle
Rectangle.present(clear=True, update=False)


# Present the fixation cross
fixation.present(clear=False, update=True)

# Leave the fixation on-screen for 500 ms
exp.clock.wait(500)

# Present the rectangle
Rectangle.present(clear=True, update=True)


# Leave the rectangle on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
