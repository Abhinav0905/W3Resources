class CreateHistogram():

    @staticmethod
    def _take_input():
        x = input("Enter the values seperated by spaces: ").split()
        x = [int(i) for i in x]
        return x 
    
    def __init__(self):
        self.x = self._take_input()
    

    def create_hsistogram(self,x):
        result = []
        for value in self.x:
            histogram_bar = '*' * value
            result.append(f"{value}: {histogram_bar}")
        return result
        
if __name__ =="__main__":
    obj = CreateHistogram()
    result = obj.create_hsistogram(obj.x)
    for line in result:
        print(line)
        
    