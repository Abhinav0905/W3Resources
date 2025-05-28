class IsStringModifier():
    @classmethod
    def _take_input(cls) -> str:
        cls.text = input("Enter Any text: ")
        return cls.text
    
    def __init__(self) -> None:
        self.text = self._take_input()

    def check_text(self) -> str:
        if len(self.text) < 2:
            return self.text
        elif len(self.text) >=2 and self.text[:2] == "Is":
            return self.text
        else:
            len(self.text) >=2 and self.text != "Is"
            return "Is" + self.text
        
if __name__ == "__main__":
    obj = IsStringModifier()
    result = obj.check_text()
    print(result)
         