import pomodoro as ptimer
import Repetition_log as rl
import book_rep
import time

def option_list():
    print('1 - Pomodoro')
    print('2 - Add Topic')
    print('3 - List Topics')
    print('4 - List Books')
    user_input = input('Select Option:')
    try:
        user_input = int(user_input)
    except ValueError:
        print('Please input a valid list number')
        time.sleep(1)
        option_list()
    if user_input == 1:
        ptimer.pomodoro_timer(int(input('Session Length:')))
    if user_input == 2:
        topic = input('Topic: ')
        subject = input('Subject: ')
        rl.new_topic(topic, subject)
        option_list()
    if user_input == 3:
        rl.list_topics()
        print("To inspect object, input it's id number.")
        print('To log a repetetion, input "rep".')
        print('To return to list, input "list".')
        rep_input = input('Input: ')
        if rep_input == 'rep':
            object_input = int(input('Which list item?'))
            rl.add_rep(object_input)
            option_list()
        if rep_input == 'list':
            option_list()
        elif int(rep_input) in range(len(rl.object_list)):
            print(rl.inspect_object(int(rep_input)))
            rep_after_inspect_input = input('Do you want to repeat this item?').lower()
            if rep_after_inspect_input == 'yes':
                rl.add_rep(int(rep_input))
            option_list()
    elif user_input > 3:
        print('Please input a valid option.')
        time.sleep(1)
        option_list()
option_list()