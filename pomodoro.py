import time
def pomodoro_timer(time):
    while time > 0:
        mins, secs = divmod(time, 60)
        current_timer = '{mins}:{secs}'.format(mins = mins, secs = secs)
        print(current_timer, end = '\r')
        time.sleep(1)
        time -= 1
    

    
