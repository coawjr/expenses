import datetime

class Calendar:
    #def __inin__(self):
      #self.calendar = datetime.datetime.now()

    def get_calendar():
       calendar = datetime.datetime.now()
       date = calendar.strftime('%Y/%m/%d')
       time = calendar.strftime('%X')
       return (str(date), str(time))