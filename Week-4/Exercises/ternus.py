""" Global settings """
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_BLACK, C_RED, C_YELLOW, C_BLUE, C_WHITE

exp = design.Experiment(name="timing puzzle")
control.set_develop_mode()
control.initialize(exp)
exp.screen.colour = C_WHITE

""" Stimuli generation """

fps = 60
mspf = 1000/fps

def load(stims):
    for i in stims:
        i.preload()

def timed_draw(stims):
    time_s = exp.clock.time
    exp.screen.clear()
    for i in stims:
        if len(stims) == 0:
            raise ValueError("There should be at least one stimuli!")
        else:
            i.present(False, False) 
    exp.screen.update()
    time_e = exp.clock.time - time_s
    return time_e
    # return the time it took to draw

def present_for(stims, num_frames=20): 
    if (mspf * num_frames - timed_draw(stims)) >= 0:
        exp.clock.wait(mspf * num_frames - timed_draw(stims))
    else:
        exp.clock.wait(timed_draw(stims))
    exp.screen.clear()
    exp.screen.update()
    

def create_circles(radius=70, space = 10):
    circle_positions = []
    for i in range(4):
        position = (-3*radius - 3*space/2 + i*2*radius + i*space, 0)
        circle_positions.append(position)
    circles = []
    for i in range(4):
        circle = stimuli.Circle(radius=radius, position=circle_positions[i], colour=C_BLACK, anti_aliasing=True)
        circles.append(circle)
    return circles

def add_tags(stims):
    colours = [C_RED, C_YELLOW, C_BLUE]
    for i in range(4):
        stimuli.Circle(radius=10, colour=colours[i%3]).plot(stims[i])

""" Trial run"""
def run_trial(circle_radius=70, inter_stimulus_interval=5, colour_tag=True):
    stims = create_circles(radius=circle_radius, space=circle_radius/7)
    load(stims)
    while True:
        present_for(stims[0:3], num_frames=inter_stimulus_interval)
        present_for(stims[1:4], num_frames=inter_stimulus_interval)
        if exp.keyboard.check(K_SPACE): 
            break
    print(timed_draw(stims))
    if  colour_tag:
        for i in stims:
            i.unload()
        add_tags(stims)
        load(stims)
        while True:     
            present_for(stims[0:3], num_frames=inter_stimulus_interval)
            present_for(stims[1:4], num_frames=inter_stimulus_interval)
            if exp.keyboard.check(K_SPACE): 
                break
        while True:
            present_for(stims[0:3], num_frames=inter_stimulus_interval+20)
            present_for(stims[1:4], num_frames=inter_stimulus_interval+20)
            if exp.keyboard.check(K_SPACE): 
                break

run_trial()



# End the current session and quit expyriment
control.end()
