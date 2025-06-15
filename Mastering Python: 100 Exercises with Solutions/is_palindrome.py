class IsPalindrome:

    s = "Liril"

    @classmethod
    def is_palindrome(cls):
        a = cls.s.lower()
        if a == a[::-1]:
            print("yes")
            return True
        else:
            print("No")
            return  False

if __name__ == "__main__":
    obj = IsPalindrome
    values = obj.is_palindrome()
    print(values)
           