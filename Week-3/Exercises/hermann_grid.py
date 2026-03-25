from expyriment import design, control, stimuli
from expyriment.misc import constants 


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "grid")
control.set_develop_mode()

#Hermann grid creator
def hermann_grid(size, colour, space, rows, columns, bg_colour):
    #Background colour
    exp.screen.colour = bg_colour
    
    #Square width and height
    sq_w, sq_h = size
    #Width and height of the whole grid 
    grid_w = sq_w * columns + (columns-1) * space
    grid_h = sq_h * rows + (rows-1) * space
    
    #List of the positions for all squares
    pos_list = []
    #List of square objects
    sq_list=[]
    #Get all the square positions
    for x in range (columns):
        for y in range (rows):
            p = (-grid_w/2 + sq_w/2 + sq_w * x + space * x, grid_h/2 - sq_h/2 - sq_h * y - space * y)
            pos_list.append(p)
        #Create square objects
        for i in pos_list:
            squares = stimuli.Rectangle(size=size, position=i, colour=colour)
            sq_list.append(squares)
    
    #Present the squares as a Hermann grid
    exp.screen.clear()
    for i in sq_list:
        if sq_list.index(i) < len(sq_list)-1:
            i.present(False, False) 
        else: 
            i.present(False, True)
    
# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#Create a hermann grid 
hermann_grid((50, 50), constants.C_BLACK, 5, 10, 10, constants.C_WHITE)

# Leave them on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
    


