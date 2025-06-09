class ExtractOddNumber():

    lst = [2,3,4,5,6,7,8,9,10]

    @classmethod
    def extract_odd(cls) -> list:
        a = cls.lst
        odd_lst = [x for x in a if x % 2 !=0]
        return odd_lst
    
if __name__ == "__main__":
    obj = ExtractOddNumber()
    result = obj.extract_odd()
    print(result)