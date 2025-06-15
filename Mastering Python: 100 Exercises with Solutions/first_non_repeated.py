class FirstNonRepeated:

    s = "swiss"

    @classmethod
    def count_of_words(cls):
        text = cls.s
        char_count ={}

        for char in text:
            char_count[char] = char_count.get(char,0)

        for char in text:
            if char_count[char] == 1:
                return char
    
        return None

if __name__ == "__main__":
    obj = FirstNonRepeated()
    result = obj.count_of_words()
    print(result)
