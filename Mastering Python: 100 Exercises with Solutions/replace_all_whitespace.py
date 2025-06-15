class ReplaceAllWhiteSpace:

    s = " a b c d  "
    
    @staticmethod
    def replace_whitespace(text):
        converted_text = text.strip()
        return converted_text

if __name__ == "__main__":
    obj = ReplaceAllWhiteSpace()
    abc = obj.replace_whitespace(obj.s)
    print(abc)