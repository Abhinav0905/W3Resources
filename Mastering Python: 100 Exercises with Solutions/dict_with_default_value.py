class DictWithDefaultValue:

    key = ['abc', 'def', 'ghi']
    value = 0

    @classmethod
    def dict_with_default_value(cls):
        a = cls.key
        b = cls.value
        # new_dict = dict(zip(a,b))
        new_dict = {k:b for k in a }
        return new_dict
    
    
if __name__ == "__main__":
    obj = DictWithDefaultValue
    values = obj.dict_with_default_value()
    print(values)