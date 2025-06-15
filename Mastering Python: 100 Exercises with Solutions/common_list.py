class CommonItems:
    lst1 = [1,23,3,4,5]
    lst2 = [1,2,3,4,7]

    @classmethod
    def find_common(cls):
        a = cls.lst1
        b = cls.lst2
        common = set(set(a) & set(b))
        # print (common)
        return common

    @classmethod
    def find_common1(cls):
        a = cls.lst1
        b = cls.lst2
        c = []
        for x in a:
            for y in b:
                if x == y:
                    c.append(x)
        return c
    
if __name__ == "__main__":
    obj = CommonItems()
    red = obj.find_common()
    red1 = obj.find_common1()
    print(red)
    print(red1)
        




