# implementation of card game - Memory

import simplegui
import random


complete_list = []
complete_list = range(8) + range(8)
state = 0
ll = 0
canvas_size = [800,100]
width_bucket = 0
height_bucket = 0
exposed = []
buckets_coordinates = []
state = 0
unpaired = 0
paired = 0
counter = 0

# helper function to initialize globals
def new_game():
    global first_eights, second_eights, complete_list
    global state, ll, width_bucket, height_bucket, exposed
    global canvas_size, buckets_coordinates, counter
    global complete_list
    width_bucket = canvas_size[0] / 16
    height_bucket = canvas_size[1]
    state = 0
    random.shuffle(complete_list)
    ll = len(complete_list)
    exposed = []
    exposed = [False for i in range(ll)]
    x = 50
    y = height_bucket
    buckets_coordinates.append([(0, 0), (50, 0), (50, 100), (0, 100)])
    for i in range(ll):
        buckets_coordinates.append([(x,0), (x+50,0), (x+50,y),(x,y)])
        x += 50
    counter = 0

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global width_bucket, state, exposed, complete_list
    global unpaired, paired, counter
    #if the card is fliped, nothing happens
    if not (exposed[pos[0] / width_bucket]):
       #if the state is zero no click that provoked a card flip
       #change state to one, mark the card as fliped
       if state == 0:
          state = 1		# flip first card
          unpaired = (pos[0] / width_bucket)
          exposed[unpaired] = True
          counter += 1

       #if the state is one, there was a click that
       #change state to two, mark the card as fliped
       elif state == 1:
           if not (exposed[pos[0] / width_bucket]): 
              state = 2        # flip second card
              paired = (pos[0] / width_bucket)
              exposed[paired] = True
              counter  += 1
        #if the state is two, the turn is over
        #time to decide whther the flipped cards are equal or not
        #change the state to one, as starting new turn
       elif state == 2:
          state = 1
          if complete_list[unpaired] != complete_list[paired]:
              exposed[unpaired] = False
              exposed[paired] = False 
          unpaired = (pos[0] / width_bucket)
          exposed[unpaired] = True
          paired = 0

       
def buttonclick():
    global first_eights, second_eights, complete_list
    global state, ll, width_bucket, height_bucket, exposed
    global canvas_size, buckets_coordinates, counter
    new_game()   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global complete_list, ll, canvas_size, ll, counter
    global width_bucket, height_bucket, buckets_coordinates
    x = 5
    y = 70
    #canvas.draw_polygon(buckets_coordinates[0], 1, 'Red',  'Green')
    #canvas.draw_polygon(buckets_coordinates[1], 2, 'Red',  'Green')
    label.set_text(str(counter))
    for i in range(ll): 
        if not exposed[i]:
           canvas.draw_polygon(buckets_coordinates[i], 2, 'Red',  'Green')
        else:
           canvas.draw_text(str(complete_list[i]), (x,y), 70, 'Red')
        x += 50
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()