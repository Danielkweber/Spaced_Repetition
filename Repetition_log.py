from datetime import date
import json

class Rep_Log():
    def __init__(self, topic, subject):
        self.topic = topic
        self.subject = subject
        self.times_reviewed = 0
        #Change Date Format
        self.dates_reviewed = [date.today().isoformat()]
        self.notes = {}
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
        return "Topic: {self.topic} \n Subject: {self.subject} \n Times Reviewed: {self.times_reviewed} \n Review Dates: {self.dates_reviewed} \n Notes: {self.notes}".format(self=self)

#class myJsonEncoder(json.JSONEncoder):
#    def default(self, obj):
#        if isinstance(obj, Rep_Log):
#            return {"Topic":obj.topic,"Subject":obj.subject,"Times Reviewd":obj.times_reviewed,"Complete":obj.is_completed,"Dates Reviewed":obj.dates_reviewed}
#        # Let the base class default method raise the TypeError
#        return json.JSONEncoder.default(self, obj)
#
#Science = [Rep_Log('Science',"otherthing"),Rep_Log('Science',"otherthing"),Rep_Log('Science',"otherthing"),Rep_Log('Science',"otherthing")]
#print(Science)
#jsons  = json.dumps(Science,cls=myJsonEncoder)
#print(jsons)

t1 = Rep_Log('Chain', 'Math')
print(t1)
t1.topic_reviewed()
print(t1)