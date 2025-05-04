import datetime
class DateTimeDisplay():
    @classmethod
    def date_time(cls):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ =="__main__":
    a=DateTimeDisplay.date_time()
    print(a)
        