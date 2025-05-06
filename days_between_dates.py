from datetime import date

class DaysBetweenDates():

    date1 = date(2014,7,2)
    date2 = date(2014,7,11)

    # def _transform_date(self):
    #     date_a = date(self.date1)
    #     date_b = date(self.date2)
    #     return date_a , date_b
    
    def date_difference(self):
        date_diff = self.date2 - self.date1
        return date_diff
    
if __name__ == "__main__":
    obj = DaysBetweenDates()
    avdf = obj.date_difference()
    print(avdf)