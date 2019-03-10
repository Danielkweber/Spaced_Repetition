import time
class Rep_Log():
    def __init__(self, topic):
        self.topic = topic
        self.times_reviewed = 0
        self.is_completed = False
        self.dates_reviewed = []
    def __str__(self):
        return "Topic: {self.topic} \n Times Reviewed: {self.times_reviewed} \n Complete: {self.is_completed} \n Review Dates: {self.dates_reviewed}".format(self=self)
    def json_encoder(self):
        pass
    def json_decoder(self):
        pass
Science = Rep_Log('Science')
print(Science)