""" Global setting """
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_RIGHT, K_LEFT
import random
exp = design.Experiment(name="key")
control.set_develop_mode()
control.initialize(exp)
""" Create stimuli """
instruction = "Press a key to indicate the position of the circle. If the circle is on the left of the screen, press 'Left_arrow'; if the circle is on the right, press 'Right_arrow'. Press 'Space' to continue."
text_instruction = stimuli.TextBox(instruction, size=(600, 300), text_size=25, position=(0, 0))
text_feedback1 = stimuli.TextLine("Correct!")
text_feedback2 = stimuli.TextLine("Wrong!")
cl = stimuli.Circle(radius=30)
rec = stimuli.Rectangle(size=(50, 50))
for i in [text_instruction, text_feedback1, text_feedback2, cl, rec]:
    i.preload()

""" Run trials """
def run_trials(trial_nums=5):
    text_instruction.present(True, True)
    exp.keyboard.wait()
    correct = 0
    for i in range(trial_nums):
        t0 = exp.clock.time
        r = random.choice([-1, 1])
        cl.reposition((r * 100, 0))
        rec.reposition(((-r) * 100, 0))
        cl.present(True, False)
        rec.present(False, True)
        key, t= exp.keyboard.wait(keys=[K_RIGHT, K_LEFT])
        t1 = t - t0
        exp.add_data_variable_names(["Key", "RT"])
    
        if (r == -1 and key == K_LEFT) or (r == 1 and key == K_RIGHT):
            text_feedback1.present(True, True)
            correct += 1
        else:
            text_feedback2.present(True, True)
        exp.clock.wait(700)
        
    text_feedback_final = stimuli.TextLine(f"Correct: {correct}     Wrong: {trial_nums-correct}")
    text_feedback_final.present(True, True)

run_trials(1)

exp.keyboard.wait()
control.end()

