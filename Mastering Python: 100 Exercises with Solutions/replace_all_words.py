class ReplaceAllWords:

    s = "Hello world, welcome to the world of Python family."

    @staticmethod
    def _replace_words(text):
        converted_str = text.replace("world","Universe")
        return converted_str

if __name__ == "__main__":
    obj = ReplaceAllWords()
    result = obj._replace_words(obj.s)
    print(result)
