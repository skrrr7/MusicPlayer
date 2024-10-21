import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Spotify-Inspired Music Player")
screen.setup(width=600, height=400)
screen.bgcolor("#1DB954")  

# Register the GIF image shapes
frame_names = ["gif/1.gif", "gif/2.gif", "gif/3.gif", "gif/4.gif"]
for frame in frame_names:
    screen.register_shape(frame)


music_turtle = turtle.Turtle()
music_turtle.shape(frame_names[0]) 
music_turtle.penup()
music_turtle.goto(0, 0)  
music_turtle.showturtle()  

# Create a turtle to display the current state at the top
state_indicator = turtle.Turtle()
state_indicator.hideturtle()
state_indicator.penup()
state_indicator.goto(0, 120) 
state_indicator.color("white")  

# Create a turtle for the timer line at the bottom
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(-250, -150)  
timer_turtle.pendown()
timer_turtle.color("black")  
timer_turtle.width(20)
timer_turtle.setheading(0)

# Create a turtle for displaying the elapsed time below the black line
elapsed_time_display = turtle.Turtle()
elapsed_time_display.hideturtle()
elapsed_time_display.penup()
elapsed_time_display.goto(-15, -190) 
elapsed_time_display.color("black")  

# Global variables
elapsed_time = 0
running = False
frame_index = 0
music_ended = False  

# State map for displaying the current state
states = {
    "STOPPED": "STOPPED",
    "PLAYING": "MUSIC PLAYING",
    "PAUSED": "MUSIC PAUSED",
    "ENDED": "MUSIC ENDED"
}

# Function to update the state indicator
def update_state(new_state):
    global state
    state = new_state
    state_indicator.clear()
    state_indicator.write(states[state], align="center", font=("Arial", 24, "bold"))
    screen.update()  

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

# Function to update the elapsed time display
def update_elapsed_time():
    elapsed_time_display.clear()
    elapsed_time_display.write(format_time(elapsed_time), align="center", font=("Arial", 16, "normal"))

def animate_music():
    global frame_index
    if running:
        music_turtle.shape(frame_names[frame_index])  
        frame_index = (frame_index + 1) % len(frame_names)
        screen.ontimer(animate_music, 100)  

# Function to play music
def play_music():
    global running, music_ended
    if not running and not music_ended:  
        running = True
        update_state("PLAYING")
        screen.ontimer(music_timer, 1000)  
        animate_music() 

# Function to pause music
def pause_music():
    global running
    running = False
    update_state("PAUSED")

# Function to stop music
def stop_music():
    global running, elapsed_time, music_ended
    running = False
    music_ended = False  
    reset_timer()
    update_state("STOPPED")

# Timer function to manage playback duration
def music_timer():
    global elapsed_time, running, music_ended
    if running and elapsed_time < 30:
        timer_turtle.forward(17)  
        elapsed_time += 1
        update_elapsed_time() 
        screen.ontimer(music_timer, 1000)  
    elif elapsed_time >= 30:
        running = False
        music_ended = True  
        update_state("ENDED")  
        music_turtle.hideturtle() 
        timer_turtle.hideturtle() 
        elapsed_time_display.clear()  

# Function to reset the timer and line
def reset_timer():
    global elapsed_time
    elapsed_time = 0
    timer_turtle.clear()
    timer_turtle.penup()
    timer_turtle.goto(-250, -150)
    timer_turtle.pendown()
    timer_turtle.setheading(0)
    update_elapsed_time()

# Key bindings
screen.listen()
screen.onkey(play_music, "p")  # Press 'p' to play
screen.onkey(pause_music, "a")  # Press 'a' to pause
screen.onkey(stop_music, "s")   # Press 's' to stop

# Initial state
state = "STOPPED"
update_state(state)

# Keep the window open
screen.mainloop()
