class ConvertDictToTuple:

    d = {'a': 1, 'b': 2, 'c': 3}

    @classmethod
    def _convert_to_tuple(cls):
        a = cls.d
        converted = list(a.items())
        return converted

if __name__ == "__main__":
    obj = ConvertDictToTuple
    values = obj._convert_to_tuple()
    print(values)