class ReverseEachWord:

    s = "Hello             World"

    @classmethod
    def reverse_each_word(cls):
        c = cls.s.split()
        print(c)
        reverse_str = ''.join(word[::-1] for word in c)
        print(reverse_str)
        return reverse_str

if __name__ == "__main__":
    obj = ReverseEachWord.reverse_each_word()
    print(obj)