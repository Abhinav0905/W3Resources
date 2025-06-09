class ReplaceOddNumberWithOne():

    lst = [1,2,3,4,5,6,7,8,9,10,11,12]

    @classmethod
    def replace_with(cls) -> list:
        a = cls.lst
        modified_lst = []
        # odd_numbers = [x for x in a if x%2 !=0]
        odd_numbers = [-1 if x%2 != 0 else x for x in a]
        modified_lst.append(odd_numbers)
        return modified_lst
    
if __name__ == "__main__":
    obj = ReplaceOddNumberWithOne()
    result = obj.replace_with()
    print(result)
    
