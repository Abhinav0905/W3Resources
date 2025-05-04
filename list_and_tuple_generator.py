class ListAndTupleGenerator():
    @classmethod
    def take_input_from_user(cls):
        nums = (input("Enter four numbers: "))
        x,y,z,a = map(int, nums.split())
        return x,y,z,a
    
    @staticmethod
    def list_generator():
        values = ListAndTupleGenerator.take_input_from_user()
        x = list[values]
        y = tuple(values)
        return x, y
    
if __name__ == "__main__":
    a = ListAndTupleGenerator.list_generator()
    print(f"List & tuple are as follows {a}")

    
