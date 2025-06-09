class ConvertIntoBool():

    lst = [-1,-2,3,-44,5,6,0,-7,0]

    @classmethod
    def convert_into_bool(cls) -> bool:
        a = cls.lst
        modified_lst = [bool(x) for x in a]
        return modified_lst
    
if __name__ == "__main__":
    obj = ConvertIntoBool()
    result = obj.convert_into_bool()
    print(result)

    