class UniqueColorFinder():

    color_list1 = set(["red","blue","green"])
    color_list2 = set(["red", "purple", "gray"])

    def print_unique_colors(self, color_list1, color_list2):
        result = []
        for a in self.color_list1:
            for b in self.color_list2:
                if a == b:
                    result.append(a)
        return result
    
if __name__ == "__main__":
    obj = UniqueColorFinder()
    abc = obj.print_unique_colors(obj.color_list1, obj.color_list2)  # Pass arguments
    print(abc)
            
