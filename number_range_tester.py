class NumberRangeTester():
    @staticmethod
    def _take_input() -> int:
        x = int(input("Enter the number: "))
        return x
    
    def range_tester(self) -> bool:
        user_input = self._take_input()
        return ((abs(1000 -user_input)<=100) or (abs(2000-user_input)<=100))
    
if __name__ == "__main__":
    tester = NumberRangeTester()
    result = tester.range_tester()
    print(result)