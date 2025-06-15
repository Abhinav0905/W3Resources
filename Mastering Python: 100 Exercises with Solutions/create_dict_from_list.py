class CreateDictFromList:

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    @classmethod
    def create_dict(cls):
        a = cls.keys
        b = cls.values
        merged_dict = dict(zip(a,b))
        return merged_dict
    
if __name__ == "__main__":
    obj = CreateDictFromList
    values = obj.create_dict()
    print(values)