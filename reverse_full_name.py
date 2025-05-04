class ReverseFullName():
    @classmethod
    def reverse_name(cls, name="Abhinav"):
        reversed_name = name[::-1]
        return reversed_name
    
if __name__ == "__main__":
    y = ReverseFullName.reverse_name("Abhinav")
    print(f"The reveerse name is {y}")
        