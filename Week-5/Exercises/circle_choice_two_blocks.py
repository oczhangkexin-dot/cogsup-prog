""" Global setting """
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_RIGHT, K_LEFT
import random
exp = design.Experiment(name="key")
control.set_develop_mode(False)
control.initialize(exp)
exp.add_data_variable_names(["Block", "Trials", "Condition", "Key", "Response", "RT"])
""" Create stimuli """
instruction = "Press a key to indicate the position of the circle. If the circle is on the left of the screen, press 'Left_arrow'; if the circle is on the right, press 'Right_arrow'. Press 'Space' to continue."
text_instruction = stimuli.TextBox(instruction, size=(600, 300), text_size=25, position=(0, 0))
text_feedback1 = stimuli.TextLine("Correct!")
text_feedback2 = stimuli.TextLine("Wrong!")
fix = stimuli.FixCross()
cl = stimuli.Circle(radius=30)
rec = stimuli.Rectangle(size=(50, 50))
for i in [text_instruction, text_feedback1, text_feedback2, cl, rec, fix]:
    i.preload()

""" Run trials """
def run_trials(trials_per_block=5, block_condition=["deterministic", "stochastic"]):
    text_instruction.present(True, True)
    exp.keyboard.wait()
    fix.present(True, True)
    exp.clock.wait(1500)
    correct = 0
    trial_counter = 0
    block_counter = 0
    R = random.choice([-1, 1])
    for i in range(trials_per_block * len(block_condition)):
        trial_counter += 1
        if trial_counter > trials_per_block:
            block_counter += 1
            trial_counter = 1
        r = random.choice([-1, 1]) if block_condition[block_counter] == "stochastic" else R
        cl.reposition((r * 100, 0)) 
        rec.reposition(((-r) * 100, 0))
        cl.present(True, False)
        rec.present(False, True)
        key, t= exp.keyboard.wait(keys=[K_RIGHT, K_LEFT])
        if (r == -1 and key == K_LEFT) or (r == 1 and key == K_RIGHT):
            text_feedback1.present(True, True)
            correct += 1
            fdbk = "correct"
        else:
            text_feedback2.present(True, True)
            fdbk= "wrong"
        exp.clock.wait(700)
        exp.data.add([block_counter+1, trial_counter+trials_per_block*block_counter, block_condition[block_counter], key, fdbk, t])
    text_feedback_final = stimuli.TextLine(f"Correct: {correct}     Wrong: {trials_per_block*len(block_condition)-correct}")
    text_feedback_final.present(True, True)


control.start()
run_trials(5)
exp.keyboard.wait()
control.end()

