import user_input as ui
import Repetition_log as rl
import JsonStorage as js

try:
    js.json_load('RepLogData.json')
except FileNotFoundError:
    pass
ui.option_list()

