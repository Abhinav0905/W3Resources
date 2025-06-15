import random

class RandomMatrixWithNormalization:

    def normalize(self):
        matrix = [[random.random() for _ in range(3)] for _ in range(3)]
        mean = sum(sum(row) for row in matrix)/9
        std = (sum((x-mean)**2 for row in matrix  for x in row/9)**0.5)
        normalized_matrix = [[(x-mean)/std for x in row] for row in matrix]
        print(normalized_matrix)
        return normalized_matrix
    
if __name__ == "__main__":
    obj = RandomMatrixWithNormalization()
    red = obj.normalize()
    print(red)


    
    
