class ConvertToCharacter:

    s = "Hello"

    @staticmethod
    def convert_to_char(text):
        converted_str = list(text)
        return converted_str

if __name__ == "__main__":
    obj = ConvertToCharacter()
    result = ConvertToCharacter.convert_to_char(obj.s)
    print(result)


    
