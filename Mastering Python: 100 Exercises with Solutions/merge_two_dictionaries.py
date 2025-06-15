class MergeTwoDictionary:

    dict1 = {'a':1, 'b':2}
    dict2 = {'b':3, 'd':4}

    @classmethod
    def merge_two_dict(cls):
        merged_dict = {**cls.dict1, **cls.dict2}
        return merged_dict

if __name__ == "__main__":
    obj = MergeTwoDictionary()
    dicst1 = obj.merge_two_dict()
    print(dicst1)
