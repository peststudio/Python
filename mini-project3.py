# template for "Stopwatch: The Game"
import simpleguitk as simplegui
# define global variables
global time
global success
global total
global stopped
time = 0
success = 0
total = 0
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_second = t % 10
    seconds = t / 10
    second = seconds % 60
    minute = seconds / 60
    if second < 10:
        str_second = '0' + str(second)
    else:
        str_second = str(second)
    value = str(minute) + ':' + '%02d' % second + '.' + str(tenth_second)
    return value

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global stopped
    timer.start()
    stopped = False
    
def stop_timer():
    global stopped
    global success
    global total
    global time
    if stopped == False:
        timer.stop()
        stopped = True
        total = total + 1
        if time % 10 == 0:
            success = success + 1
    
    
def reset_timer():
    global time
    global stopped
    global success
    global total
    timer.stop()
    time = 0
    success = 0
    total = 0
    stopped = True
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1

# define draw handler
def draw(canvas):
    #canvas.draw_line
    global time
    global success
    global total
    formatted_time = format(time)
    canvas.draw_text(formatted_time, (80, 120), 50, 'Green')
    canvas.draw_text(str(success) + '/' + str(total),(240,30),30, 'Green') 
# create frame
frame = simplegui.create_frame('Stopwatch',300,200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start',start_timer,100)
frame.add_button('Stop',stop_timer,100)  
frame.add_button('Reset',reset_timer,100)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

