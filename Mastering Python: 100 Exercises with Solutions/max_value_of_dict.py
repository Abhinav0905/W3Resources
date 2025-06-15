class MaxValueOfDict:

    dict1 = {'a':1, 'b':45, 'c':45.1, 'd':43}

    @classmethod
    def max_value_of_dict(cls):
        a = cls.dict1
        maxvalue = max(a.values())
        return maxvalue
    
if __name__ == "__main__":
    obj = MaxValueOfDict
    values = obj.max_value_of_dict()
    print(values)