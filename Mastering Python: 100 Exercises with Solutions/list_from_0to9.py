class ListOfvalues():
    @staticmethod
    def list_of_values(num:int) -> list:
        result = list(range(num))
        return result
    
if __name__ == "__main__":
    obj = ListOfvalues()
    values = obj.list_of_values(10)
    print(values)