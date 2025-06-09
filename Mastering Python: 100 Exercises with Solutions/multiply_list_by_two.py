class MultiplyNumberList():
    
    @staticmethod
    def _take_input() -> list:
        numbers = list(map(int, input("Enter the numbers seperated by space: ").split()))
        return numbers
    
    def __init__(self):
        self.numbers = self._take_input()

    def mul_the_list(self):
        num = self.numbers
        multiplied_list = [x**2 for x in num]
        return multiplied_list
    
if __name__ == "__main__":
    obj = MultiplyNumberList()
    result = obj.mul_the_list()
    print(f"the multipled list is {result}")



