class EventOddchecker():

    @staticmethod
    def _take_inpu() -> None:
        x = int(input("Enter the number:  "))
        return x
    
    def __init__(self) -> None:
        self.x = self._take_inpu()


    def is_prime(self,x) -> bool:
        if self.x % 2 != 0:
            return "The number is a odd number"
        else:
            return "The numer is an odd number"
        
if __name__ == "__main__":
    obj = EventOddchecker()
    result = obj.is_prime(obj.x)
    print(result)
