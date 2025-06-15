class SortDictionaryByKey:

    lst = [{'name': 'Abhinav', 'age': 25}, {'name': 'Richa', 'age':25}, {'name': 'Abhishek', 'age':30}]

    @classmethod
    def sort_dict(cls):
        a = cls.lst
        sorted_list = sorted(a, key=lambda x:x['age'])
        return sorted_list

if __name__ == "__main__":
    obj = SortDictionaryByKey()
    abcd = obj.sort_dict()
    print(abcd)