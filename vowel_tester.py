class VowelTester():

    @staticmethod
    def _take_input() -> str:
        x = input("Enter the string: ")
        return x 
    
    def __init__(self):
        self.x = self._take_input()

    def check_vowel(self,x):
        vowels = ['a','e','i','o','u']

        for i in self.x:
            if i in vowels:
                return "the given word is a vowel"
            else:
                return "not a vowels"
            
if __name__ == "__main__":
    obj = VowelTester()
    abc = obj.check_vowel(obj.x)
    print (abc) 
