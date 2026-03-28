from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_1, K_2, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(-300,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial():
    instruction = "Cover your eye on the same side of the cross. Stare at the cross with the other eye. You can adjust the position (with left and right arrow keys) and size (with key 1 for smaller and key 2 for bigger) of the circle. Press Space to continue."
    text_instruction = stimuli.TextBox(instruction, size=(500, 300), text_size=30, position=(0, 0), text_justification=0)
    text_instruction.preload()
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)
    
    
    key_list = [K_RIGHT, K_LEFT, K_2, K_1]
    text_instruction.present(True, True)
    exp.keyboard.wait()
    while True:
        fixation.present(True, False)
        circle.present(False, True)
        fx, fy = fixation.position
        cx, cy = circle.position
        zoom = {K_1: -1, K_2: 1}
        key_move, t = exp.keyboard.wait(keys=key_list+[K_SPACE])
        if (key_move == K_RIGHT and cx < fx) or (key_move == K_LEFT and cx > fx): 
            circle.reposition((fx, fy))
            fixation.reposition((cx, cy))
        elif key_move in [K_2, K_1]:
            circle.unload()
            circle.scale(factors=(1 + 0.1*zoom[key_move], 1 + 0.1*zoom[key_move]))
            circle.preload()
        elif key_move == K_SPACE:
            break   

control.start(subject_id=1)

run_trial()
    
control.end()