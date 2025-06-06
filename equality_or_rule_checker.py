class EqualityChecker():

    @staticmethod
    def _take_input():
        numbers = input("Enter the numbers: ").split()
        a,b = map(int, numbers)
        return a,b
    
    def __init__(self):
        self.a, self.b = self._take_input()

    def conditional_checker(self) -> bool:
        a,b = self.a, self.b

        if a == b:
            return True
        elif a - b == 5:
            return True
        else:
            return False
        
if __name__ == "__main__":
    obj = EqualityChecker()
    result = obj.conditional_checker()
    print(result)