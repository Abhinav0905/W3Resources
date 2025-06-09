class ListOfNumToString():

    @staticmethod
    def _take_input():
        numbers = input("Enter the numbers followed by sapce: ").split()
        return numbers
    
    def __init__(self):
        self.numbers = self._take_input()

    def convert_num_to_str(self):
        convereted = list(map(str, self.numbers ))
        return convereted
    
if __name__ == "__main__":
    obj = ListOfNumToString()
    result = obj.convert_num_to_str()
    print(result)