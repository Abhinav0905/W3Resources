class FibboaniSeries:

    def _take_input(self):
        n = (input("Enter the number for which Fiboanni series to be generated: "))
        return n
    
    def __init__(self):
        self.n = self._take_input()

    def generate_series(self) -> list:
        fib_sequence =[0,1]
        m = int(self.n)
        while fib_sequence[-1] < m:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[:-1]

if __name__ == "__main__":
    obj = FibboaniSeries()
    result = obj.generate_series()
    print(result)
