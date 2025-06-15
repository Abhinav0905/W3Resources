class LengthOfLongestString:

    s = ["Abhinav", "Richa","Vivaan","Abhishek"]

    @classmethod
    def find_length(cls):
        a = cls.s
        max_length = []
        find_length = [len(x) for x in a ]
        max_length.append(find_length)
        find_max_lenth = max(max_length)
        return max(find_max_lenth)
    
if __name__ == "__main__":
    obj = LengthOfLongestString
    values = obj.find_length()
    print(values)
