class DictBasedOnItsValue:

    d = {'a': 1, 'b': 2, 'c': 3}

    @classmethod
    def dict_based_on_its_value(cls):
        a = cls.d
        filtered_dict = {k:v for k,v in a.items() if v > 3}
        return filtered_dict
    
if __name__ == "__main__":
    obj = DictBasedOnItsValue()
    red = obj.dict_based_on_its_value()
    print(red)
