import json
import sys
import Repetition_log as rl

class JsonTopicEncoder(json.JSONEncoder):
    def default(self, rep_obj):
        if isinstance(rep_obj, rl.RepLog):
            return {
                'Topic':rep_obj.topic, 
                'Subject':rep_obj.subject, 
                'Times Reviewed':rep_obj.times_reviewed, 
                'Dates Reviewed':rep_obj.dates_reviewed, 
                'Notes':rep_obj.notes, 
                '__RepLog__': True
                }
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, rep_obj)

object_list = list()

def json_hook(obj):
    if '__RepLog__' in obj:
        object_list = rl.RepLog(topic = obj['Topic'], subject = obj['Subject'], times_reviewed = obj['Times Reviewed'], dates_reviewed = obj['Dates Reviewed'], notes = obj['Notes'], from_file=True) 
        return object_list
    return obj

def json_load(Jsonfile):
    global object_list
    with open(Jsonfile) as f:
        object_list = json.load(f, object_hook=json_hook)

def cleanup():
    with open('RepLogData.json', 'w') as f:
        json.dump(object_list, fp = f, cls = JsonTopicEncoder, indent= 2)
    sys.exit()
