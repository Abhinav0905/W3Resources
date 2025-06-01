class StringCopyGenerator():
    @staticmethod
    def _take_input() -> tuple[str,int]:
        x = input("Enter the text that need o generate multiple times: ")
        y = int(input("Enter the number of times that need to generqated:"))
        return x,y
    
    def __init__(self) -> None:
        self.x , self.y = self._take_input()
    
    def string_copy_generator(self, x, y) -> str:
        result = ""
        for i in range(y):
            result = result + x
        return result
    
if __name__ == "__main__":
    obj = StringCopyGenerator()
    generated_text = obj.string_copy_generator(obj.x, obj.y)
    print(generated_text)

