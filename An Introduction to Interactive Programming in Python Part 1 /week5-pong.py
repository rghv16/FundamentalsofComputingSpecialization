# Author: Raghav Aterya
# Email: raghavatreya16@gmail.com
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [ WIDTH / 2, HEIGHT / 2 ]
    if direction == 'RIGHT':
        ball_vel = [random.randrange(1,10) , -random.randrange(1,10) ]
    else:
        ball_vel = [-random.randrange(1,10), -random.randrange(1,10)]



# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1 , score2, RIGHT   # these are ints
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = (HEIGHT - PAD_HEIGHT) // 2
    paddle2_pos = (HEIGHT - PAD_HEIGHT) // 2
    if RIGHT:
        spawn_ball("RIGHT")
    else:
        spawn_ball("LEFT")
    RIGHT = not RIGHT

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS
    # draw mid line and gutters
    
    canvas.draw_line([WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # keeping the ball within the height
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 7, 'Red', 'Red') 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos < 300:
        paddle1_pos = max(HALF_PAD_HEIGHT, paddle1_pos)
    else:
        paddle1_pos = min(HEIGHT-HALF_PAD_HEIGHT, paddle1_pos)

    paddle2_pos += paddle2_vel
    if paddle2_pos < 300:
        paddle2_pos = max(HALF_PAD_HEIGHT, paddle2_pos)
    else:
        paddle2_pos = min(HEIGHT-HALF_PAD_HEIGHT, paddle2_pos)
        
    # draw paddles
    # [0, width]
    # Assuming the paddle center is pad_center = ()
    canvas.draw_polygon(((0, paddle1_pos-HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT), (PAD_WIDTH ,paddle1_pos+HALF_PAD_HEIGHT), (0,paddle1_pos+HALF_PAD_HEIGHT)), 6, 'Yellow', 'Yellow')
    canvas.draw_polygon(((WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH ,paddle2_pos+HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT)), 6, 'Yellow', 'Yellow')

    # determine whether paddle and ball collide    
    # left
    if ball_pos[0] <=  BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos-HALF_PAD_HEIGHT and paddle1_pos+HALF_PAD_HEIGHT >= ball_pos[1]:
            ball_vel[0] = - ball_vel[0]
        else:
            score2 += 1
            spawn_ball('RIGHT')
    if ball_pos[0] +  BALL_RADIUS + PAD_WIDTH >= WIDTH:
        if ball_pos[1] >= paddle2_pos-HALF_PAD_HEIGHT and paddle2_pos+HALF_PAD_HEIGHT >= ball_pos[1]:
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball('LEFT')
    # draw scores
    canvas.draw_text(str(score1), (250, 50), 22, 'Yellow', 'serif')
    canvas.draw_text(str(score2), (350, 50), 22, 'Yellow', 'serif')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    # when i am pressing the button the paddle should go in any direction until i left the button
    # paddle will be moving up and down with constant speed
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 3
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 3
    # i am using this structure bcz it will work when both player simultaniously 
    # press respective key
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 3
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    # reseting the velocity to zero
    if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['up']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['w']:
        paddle2_vel = 0
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background('Green')
button1 = frame.add_button('Reset', new_game)
# start frame
new_game()
frame.start()