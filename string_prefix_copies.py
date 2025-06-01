class StringPrefixCopies():

    @staticmethod
    def _take_input():
        x = input("Enter the character: ")
        y = int(input("Enter the number of times the sub string need to print: "))
        return x , y
    
    def __init__(self):
        self.x, self.y = self._take_input()

    def string_prfix_copies(self,x,y):
        result = []

        if len(self.x) >= 2:
            prefix = self.x[:2]
            for i in range(self.y):
                result.append(prefix)
        else:
            for i in range(self.y):
                result.append(self.x)
                
        return result

if __name__ == "__main__":
    obj = StringPrefixCopies()
    abc = obj.string_prfix_copies(obj.x, obj.y)
    print(abc)

            


