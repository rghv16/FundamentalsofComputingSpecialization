'''
"Stopwatch: The Game"
Author: Raghav Atreya
email: raghavatreya16@gmail.com
http://www.codeskulptor.org/#user46_cV0vDckm7F00DR3_0.py
'''

import simplegui

# define global variables
time = 0
#  Give only one point if hitting the "Stop" button changes these numbers when the timer is already stopped.
is_stop = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# Student should add code for the format function here
# A.BC.D
def format(t):
    d = t%10
    t = t/10
    bc = t%60
    a = t/60
    BC = str(bc)
    if len(BC) == 1:
        BC = '0'+BC
    return str(a)+':'+BC+'.'+str(d)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    print "Start Button is Pressed"
    global timer, is_stop
    timer.start()
    is_stop = False

def stop_handler():
    print "Stop handler is pressed"
    global timer, win, total, time, is_stop
    timer.stop()
    if not is_stop:
        if time%10 == 0:
            win += 1
        total += 1
    is_stop = True

def reset_handler():
    global time, timer, win, total
    #stop_handler()
    time = 0
    timer.stop()
    win = 0
    total = 0
    print "Reset handler is pressed"
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1
    print "Time handler called"
    #timer.stop()
    
# define draw handler
def draw_handler(canvas):
    global time, win, total
    canvas.draw_text(format(time), (25, 150), 50, 'Blue', 'monospace')
    canvas.draw_text(str(win)+'/'+str(total), (100, 50), 25, 'Yellow',  "sans-serif")
# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200, 150)
frame.set_canvas_background('#F9C00D')

start = frame.add_button('Start ', start_handler)
stop  = frame.add_button('Stop ', stop_handler)
reset = frame.add_button('Reset ', reset_handler)

win = 0
total = 0

# register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw_handler)
frame.start()