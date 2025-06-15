class ReplaceEvenWithNegative():

    lst = [1,2,3,4,5,6,7,8,9,10]

    @classmethod
    def _replace_with_negative(cls):
        a = cls.lst
        updated_lst = [-x if x%2 == 0 else x for x in a]
        return updated_lst
    
if __name__ == "__main__":
    obj = ReplaceEvenWithNegative()
    result = obj._replace_with_negative()
    print(result)