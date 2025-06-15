from collections import Counter
class CountOccurance:

    s = "Hello World"

    @classmethod
    def calculate_occurance(cls):
        a = cls.s
        # char_count = []
        final_string = ''.join(a.split())
        final_count = Counter(final_string)
        # final_count1 = [x for x in final_string if x > 1 count(x) += 1]
        # char_count.append(final_count1)
        return final_count

if __name__ == "__main__":
    values = CountOccurance.calculate_occurance()
    print(values)