class FirstAndLastColor():
    color_list = ["abc", "Red", "Blue", "Green"]

    @classmethod
    def first_and_last_color(cls):
        return [cls.color_list[0], cls.color_list[-1]]
    
if __name__ == "__main__":
    z = FirstAndLastColor.first_and_last_color()
    print(z)


    