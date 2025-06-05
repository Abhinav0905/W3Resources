import math


class TraiangleAreaCalculator():

    @staticmethod
    def _take_input():
        triangle = input("Enter the three sides of the triangle, seperated by space: ").split()
        p,b,h = map(int, triangle)
        return p,b,h
    
    def __init__(self):
        self.a, self.b, self.c = self._take_input()
    
    def calculate_area(self):
        a,b,c = self.a, self.b, self.c

        if (a + b > c) and (a + c > b ) and (b + c > a):
            print("the given number are valid")
            s = (a+b+c)/2

            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            return area
        else:
            return "Invalid area"
        
    def calculate_area_base_height(self, base, height):
        # Using base × height formula
        return 0.5 * base * height

if __name__ == "__main__":
    obj = TraiangleAreaCalculator()
    area = obj.calculate_area()
    print(f"Area of triangle: {area}")

