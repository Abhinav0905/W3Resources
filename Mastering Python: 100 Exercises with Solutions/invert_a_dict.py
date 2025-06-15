class InvertDict:

    dict1 = {'a': 1, 'b': 2, 'c': 3}

    @classmethod
    def invert_a_dict(cls):
        a = cls.dict1
        inverted_dict = {v:k for k,v in a.items()}
        return inverted_dict
    
    
if __name__ == "__main__":
    obj = InvertDict()
    values = obj.invert_a_dict()
    print(values)