from datetime import date
import JsonStorage as js

class RepLog():
    def __init__(self, topic, subject, times_reviewed = 0, dates_reviewed = [date.today().isoformat()], notes = {}, from_file = False):
        self.topic = topic
        self.subject = subject
        self.times_reviewed = times_reviewed
        self.dates_reviewed = dates_reviewed
        self.notes = notes
        if not from_file:
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


def new_topic(topic, subject):
    obj = RepLog(topic, subject)
    js.object_list.append(obj)

def list_topics():
    for index, item in enumerate(js.object_list):
        print('{index}: {item}'.format(index = index, item = repr(item)))

def add_rep(input):
    js.object_list[input].topic_reviewed()

def inspect_object(input):
    return js.object_list[input]



