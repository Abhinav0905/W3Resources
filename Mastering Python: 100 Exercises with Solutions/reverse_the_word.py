class ReverseWord:

    s = " Hello World"

    @classmethod
    def reverse_sentense(cls):
        a = cls.s
        reverse_word = ' '.join(a.split()[::-1])
        # reverse_word = a[::-1]
        return reverse_word

if __name__ == "__main__":
    obj = ReverseWord
    values = obj.reverse_sentense()
    print(values)