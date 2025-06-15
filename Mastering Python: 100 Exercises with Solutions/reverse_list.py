class ReverseList:

    lst = [1,2,3,4,5]

    @classmethod
    def reversed_lst(cls):
        reversed_list = cls.lst[::-1]
        return reversed_list

if __name__ == "__main__":
    obj = ReverseList()
    rev = obj.reversed_lst()
    print(rev)

