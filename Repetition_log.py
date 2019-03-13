import datetime
import json

class Rep_Log():
    def __init__(self, subject, topic):
        self.topic = topic
        self.subject = subject
        self.times_reviewed = 0
        self.is_completed = False
        self.dates_reviewed = []
    def __repr__(self):
        return repr(self.topic)
    def __str__(self):
        return "Topic: {self.topic} \n Times Reviewed: {self.times_reviewed} \n Complete: {self.is_completed} \n Review Dates: {self.dates_reviewed}".format(self=self)

class myJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Rep_Log):
            return {"topic":obj.topic,"subject":obj.subject,"times_reviewd":obj.times_reviewed,"is_completed":obj.is_completed,"dates_reviewed":obj.dates_reviewed}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

Science = [Rep_Log('Science',"otherthing"),Rep_Log('Science',"otherthing"),Rep_Log('Science',"otherthing"),Rep_Log('Science',"otherthing")]
print(Science)
jsons  = json.dumps(Science,cls=myJsonEncoder)
print(jsons)