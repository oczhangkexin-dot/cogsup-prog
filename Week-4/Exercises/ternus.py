""" Global settings """
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_BLACK, C_RED, C_YELLOW, C_BLUE, C_WHITE

exp = design.Experiment(name="ternus")
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
    for i in stims:
        if len(stims) == 0:
            raise ValueError("There should be at least one stimuli!")
        elif stims.index(i) == 0:
            i.present(True, False)
        elif stims.index(i) < len(stims)-1:
            i.present(False, False)
        else:
            i.present(False, True)          
    time_e = exp.clock.time - time_s
    return time_e
    # return the time it took to draw

def present_for(stims, num_frames=20): 
    if (mspf * num_frames - timed_draw(stims)) >= 0:
        exp.clock.wait(mspf * num_frames - timed_draw(stims))
    else:
        exp.clock.wait(timed_draw(stims))
    

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
def run_trial(circle_radius=70, inter_stimulus_interval=0):
    stims = create_circles(radius=circle_radius, space=circle_radius/7) + [stimuli.Canvas(size=(1080, 1080))]
    k_check_nums = 0
    load(stims)
    while True:
        present_for(stims[0:3])
        t0 = exp.clock.time
        stims[4].present(True if inter_stimulus_interval > 0 else False, True if inter_stimulus_interval > 0 else False)
        exp.clock.wait(mspf*inter_stimulus_interval - exp.clock.time + t0)
        
        present_for(stims[1:4])
        t0 = exp.clock.time
        stims[4].present(True if inter_stimulus_interval > 0 else False, True if inter_stimulus_interval > 0 else False)
        exp.clock.wait(mspf*inter_stimulus_interval - exp.clock.time + t0)
        
        if exp.keyboard.check(K_SPACE): 
            k_check_nums += 1 
            if k_check_nums == 1:
                for i in stims:
                    i.unload()
                add_tags(stims)
                load(stims)
            elif k_check_nums == 2:
                inter_stimulus_interval += 20
            else:
                break        

control.start(subject_id=1)                                 
run_trial()
control.end()
