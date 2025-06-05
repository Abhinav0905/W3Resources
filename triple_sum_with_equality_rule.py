class TripleSumWithEqualityRule():

    @staticmethod
    def _take_input():
        numbers = input("Enter the numbers to be added, seperated by comma").split()
        a,b,c  = map(int, numbers)
        return a,b,c
    
    def __init__(self):
        self.a , self.b, self.c = self._take_input()

    def special_sum_rule(self):
        a , b , c = self.a , self.b, self.c
        if a == b or b == c or c == a:
            print("Any two values are same , hence the sum is Zero")
        else:
            result = a + b + c
            return result
    
if __name__ == "__main__":
    obj = TripleSumWithEqualityRule()
    output = obj.special_sum_rule()
    print(f"the result is {output}")
