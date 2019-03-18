import time
def pomodoro_timer(user_time):
        user_time *= 60
        while user_time > 0:
                mins, secs = divmod(user_time, 60)
                current_timer = '{mins}:{secs}'.format(mins = mins, secs = secs)
                print(current_timer, end = '\r')
                time.sleep(1)
                user_time -= 1


    
