from expyriment import design, control, stimuli
import random

def load(stims):
    for i in stims:
        i.preload()

def timed_draw(stims):
    time_e = 0
    time_s = exp.clock.time
    for i in stims:
        if stims.index(i) == 0:
            i.present(True, False)
        else:
            i.present(False, True) 
        time_e =exp.clock.time + time_e - time_s
    return time_e
    # return the time it took to draw

def present_for(stims, t=1000): 
    exp.clock.wait(t-timed_draw(stims))


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemented correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

if all(abs(d - 500) <= 1 for d in durations):
   print("Well done!")
else:
    print(f"Timing off. Measured durations were: {durations}")


control.end()