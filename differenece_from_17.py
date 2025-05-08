class Difference():
    def _take_input(self) -> int:
        x = int(input("Enter the Number: "))
        return x
    
    def calculate_difference(self,num:_take_input) -> int:
        num = self._take_input()
        get_value = num - int(17)
        if get_value > 17:
            return abs(2*get_value)
        else:
            return get_value
        
if __name__ == "__main__":
    obj = Difference()
    output = obj.calculate_difference(num=18)
    print(output)