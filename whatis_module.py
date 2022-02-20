import datetime
import random




class whatis():
    global me
    me = ["boss" , "sir"]
    def __init__(self):
        pass
        
            

    
    def time(self):
        t = datetime.datetime.now().time().strftime("%I %M %p")
        return (t.removeprefix("0") + me[random.randrange(0 , len(me))])
    def date(self):
        _day = datetime.datetime.now().date().day
        return (f"today is {_day}th" + me[random.randrange(0 , len(me))])
    def process(self , TD):
        self.Td = TD
        if self.Td == "time":
            response = self.time()
        elif self.Td == "date":
            response = self.date()
        return response
    


