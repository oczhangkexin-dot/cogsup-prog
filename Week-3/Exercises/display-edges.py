from expyriment import design, control, stimuli
control.set_develop_mode(False)
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#Start running the experiment
control.start(subject_id=1)

#Create 4 squares
r1=stimuli.Shape(position=(-932, -513), colour='black', debug_contour_colour='red')
r1.add_vertices([(54, 0), (0, 54), (-54, 0)])

r2=stimuli.Shape(position=(-932, 512), colour='black', debug_contour_colour='red')
r2.add_vertices([(54, 0), (0, -54), (-54, 0)])

r3=stimuli.Shape(position=(933, -513), colour='black', debug_contour_colour='red')
r3.add_vertices([(-54, 0), (0, 54), (54, 0)])

r4=stimuli.Shape(position=(933, 512), colour='black', debug_contour_colour='red')
r4.add_vertices([(-54, 0), (0, -54), (54, 0)])

#Present the 4 squares
r1.present(clear=True, update=False)
r2.present(clear=False, update=False)
r3.present(clear=False, update=False)
r4.present(clear=False, update=True)

# Leave them on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()