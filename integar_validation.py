class Integarvalidation():

    @staticmethod
    def _take_input():
        a,b= input("Enter the numbers: ").split()
        return a,b
    
    def __init__(self):
        self.a, self.b = self._take_input()

    def check_validation(self):
        a, b = self.a, self.b

        if type(a) == int and type(b) == int:
            return a + b
        else:
            print("Non Integer value, Can't be added")
            return None

if __name__ == "__main__":
    obj = Integarvalidation()
    result = obj.check_validation()
    print(result)


