class FindIndices:

    lst = [0,1,4,5,7,0,10]

    @classmethod
    def find_indices(cls):
        a = cls.lst
        indices = [x for x,value in enumerate(a) if value !=0]
        return indices
    
if __name__ == "__main__":
    obj = FindIndices()
    abcd = obj.find_indices()
    print(abcd)