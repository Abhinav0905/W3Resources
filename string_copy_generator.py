class StringCopyGenerator():

    @staticmethod
    def _take_input() -> int:
        text = (input("Please enter any number: "))
        x = int (text)
        return x
    
    def __init__ (self) -> None:
        self.x = self._take_input()

    def positive_string_generator(self) -> int:
        if self.x <= 0:
            return "No valid number entered, Please try again later"
        
        else:
            return str(abs(self.x))
        
        
if __name__ == "__main__":
    obj = StringCopyGenerator()
    result = obj.positive_string_generator()
    print(result)

        
