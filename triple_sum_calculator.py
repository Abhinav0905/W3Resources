class TripleSumCalculator():
    @staticmethod
    def _take_input() -> int:
        nums = (input ("Enter three numbers: "))
        x,y,z = map(int, nums.split())
        return x,y,z
    
    def __init__(self) -> None:
        self.x , self.y, self.z = self._take_input()

    def sum_three_numbers(self) -> int:
        if self.x == self.y == self.z:
            return 3*(self.x+self.y+self.z)
        else:
            return self.x + self.y + self.z
        
if __name__ == "__main__":
    sumofnumber = TripleSumCalculator()
    result = sumofnumber.sum_three_numbers()
    print(result)
         