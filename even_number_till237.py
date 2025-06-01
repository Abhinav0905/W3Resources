class EvenNumberTillANumber():

    Numbers = [1,2,3, 4,5 , 6, 27 , 80, 90, 100, 101, 103, 
               104, 107, 109, 110, 111, 250, 226, 237]
    
    @classmethod
    def print_even_number(cls) -> list:
        even_number = []
        for value in cls.Numbers:
            if value == 237:
                break
            elif value %2 == 0:
                even_number.append(value)
        return even_number
    
if __name__ == "__main__":
    obj = EvenNumberTillANumber()
    result = obj.print_even_number()
    print(result)