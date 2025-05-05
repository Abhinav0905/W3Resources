class NumberExpansionCalculator():
    @staticmethod
    def _inupt_from_user():
        x = int(input("Enetr the number to be expanded: "))
        return x
    

    @classmethod
    def number_expansion_calculator(cls):
        x = cls._inupt_from_user()
        expansion = x + x**2 + x**3
        return expansion
    
if __name__ == "__main__":
    a = NumberExpansionCalculator.number_expansion_calculator()
    print(f"the expandxed number is  {a}")
