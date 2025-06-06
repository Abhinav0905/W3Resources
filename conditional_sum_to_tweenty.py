class ConditionalSum():

    @staticmethod
    def _take_input():
        numbers = input("Enter the numbers : ").split()
        a,b,c = map(int, numbers)
        return a,b,c
    
    def __init__(self):
        self.a, self.b,self.c = self._take_input()

    def check_sum(self):
        a,b,c = self.a, self.b, self.c

        if a+b+c >= 15 and a+b+c <= 20:
            return 20
        else:
            return a + b + c

if __name__ == "__main__":
    obj = ConditionalSum()
    result = obj.check_sum()
    print(result) 
            