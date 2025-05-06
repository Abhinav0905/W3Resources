import calendar

class MonthlyCalanderDisplay():
    def _take_input(self):
        m = int(input("Enter the Month Name : "))
        y = int(input("Enter the year: "))
        return m , y
    
    def print_calander(self):
        a, b  = self._take_input()
        return (calendar.month(b,a))
    
if __name__ == "__main__":
    abc = MonthlyCalanderDisplay.print_calander()
    print(abc)
