from datetime import date
import json
import sys

class RepLog():
    def __init__(self, topic, subject, times_reviewed = 0, dates_reviewed = [date.today().isoformat()], notes = {}):
        self.topic = topic
        self.subject = subject
        self.times_reviewed = times_reviewed
        self.dates_reviewed = dates_reviewed
        self.notes = notes
        self.add_notes()
    def add_notes(self):
        self.notes[self.times_reviewed] = input('Add Notes: ')
    def topic_reviewed(self):
        self.times_reviewed += 1
        self.dates_reviewed.append(date.today().isoformat())
        self.add_notes()
    def __repr__(self):
        return repr(self.topic)
    def __str__(self):
        return "Topic: {self.topic} \n\r Subject: {self.subject} \n Times Reviewed: {self.times_reviewed} \n Review Dates: {self.dates_reviewed} \n Notes: {self.notes}".format(self=self)

class JsonTopicEncoder(json.JSONEncoder):
    def default(self, rep_obj):
        if isinstance(rep_obj, RepLog):
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
def json_load(jsonfile):
    for obj in jsonfile:
        if '__RepLog__' in obj:
            obj_to_load = RepLog(topic = obj['Topic'], subject = obj['Subject'], times_reviewed = obj['Times Reviewed'], dates_reviewed = obj['Dates Reviewed'], notes = obj['Notes'])
            object_list.append(obj_to_load)

def new_topic(topic, subject):
    obj = RepLog(topic, subject)
    object_list.append(obj)

def list_topics():
    for index, item in enumerate(object_list):
        print('{index}: {item}'.format(index = index, item = repr(item)))

def add_rep(input):
    object_list[input].topic_reviewed()

def inspect_object(input):
    return object_list[input]
def cleanup():
    with open('RepLogData.json', 'w') as f:
        json.dump(object_list, fp = f, cls = JsonTopicEncoder, indent= 2)
    sys.exit()



