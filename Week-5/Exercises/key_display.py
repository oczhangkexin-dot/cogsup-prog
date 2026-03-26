from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_1, K_2, K_RIGHT, K_LEFT

exp = design.Experiment(name="key")

control.set_develop_mode()
control.initialize(exp)
text1 = stimuli.TextLine("Press a key")
text1.present(True, True)
key, t= exp.keyboard.wait(keys=[K_1, K_2])
text2 = stimuli.TextLine(f"You pressed {key}")
text2.present(False, False)
text3 = stimuli.TextLine(f"You took {t}ms")
exp.clock.wait(1000)
text3.present(False, False)
exp.clock.wait(1000)
text4 = stimuli.TextLine()
control.end()

present instruction
present the stimuli
record the key
compare
present feedback