class ValueInGroupTester():

    @staticmethod
    def _take_input() -> int:
        x = int(input("Enter the number: "))
        return x
    
    def __init__(self) -> None:
        self.x = self._take_input()

    def value_in_group_tester(self,x) -> bool:
        num_group = [1,2,3,4,5,6,7]

        for i in chr(self.x):
            if i in num_group:
                return "True"
            else:
                return "False"
        
if __name__ == "__main__":
    obj = ValueInGroupTester()
    abc = obj.value_in_group_tester(obj.x)
    print(abc)

