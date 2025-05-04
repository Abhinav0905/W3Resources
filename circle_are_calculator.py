class CircleAreaCalculator():
    @staticmethod
    def _take_input():
        x = float(input("Enter the radius: "))
        return x
    @classmethod
    def circle_area_calculator(cls):
        radius = cls._take_input()
        area = 3.1416 * radius * radius
        return area
    
if __name__ == "__main__":
    a=CircleAreaCalculator.circle_area_calculator()
    print(f"area of the circle {a}")