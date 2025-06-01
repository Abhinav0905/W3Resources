class ListToStringConcat():

    @staticmethod
    def _take_input():
        x = input("Enter the characcter following by space: ").split()
        return x 
    
    def __init__(self) -> None:
        self.x = self._take_input()

    def concat_to_string(self,x) -> str:
        result = ''.join(self.x)
        return result
    
if __name__ == "__main__":
    obj = ListToStringConcat()
    r = obj.concat_to_string(obj.x)
    print(r)