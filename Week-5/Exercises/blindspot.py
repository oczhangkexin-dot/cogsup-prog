from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_1, K_2, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(eye):
    eyes = ['left', 'right']
    instruction = f"Cover your {eye} eye and staring at the cross with your {eyes[eyes.index(eye)-1]} eye. Using keys to adjust the position (left and right arrows) and size (1 for smaller and 2 for bigger) of the circle until you cannot see it. Press Space to continue."
    text_instruction = stimuli.TextBox(instruction, size=(600, 300), text_size=25, position=(0, 0), text_justification=0)
    text_instruction.preload()
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0] if eye == "right" else [-300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)
    
    adjusting_dict = {}
    key_list = [K_RIGHT, K_LEFT, K_UP, K_DOWN, K_2, K_1]
    for key in key_list:
        k_adjust = ({key: (-1)**key_list.index(key)})  
        adjusting_dict.update(k_adjust)
    print(adjusting_dict)

    text_instruction.present(True, True)
    exp.keyboard.wait()
    while True:
        fixation.present(True, False)
        circle.present(False, True)
        key_move, t = exp.keyboard.wait(keys=key_list+[K_SPACE])
        if key_move in [K_RIGHT, K_LEFT, K_UP, K_DOWN]: 
            if key_move in [K_RIGHT, K_LEFT]:
                circle.move(offset=(5*adjusting_dict[key_move], 0))
            else:
                circle.move(offset=(0, 5*adjusting_dict[key_move]))
        elif key_move in [K_2, K_1]:
            radius = radius + 5*adjusting_dict[key_move]
            circle = make_circle(r=radius, pos=circle.position)
        else:
            break   

control.start(subject_id=1)

run_trial("left")
    
control.end()