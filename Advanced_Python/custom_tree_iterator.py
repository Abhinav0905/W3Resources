class TreeNode:

    def __init__(self,value):
        self.value = value
        self.children = []

    
    def add_child(self, child_node):
        self.children.append(child_node)

    
class TreeIterator:
    def __init__(self,root):
        self.stack = [root]

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        for child in reversed(node.children):
            self.stack.append(child)
        return node.value
    
if __name__ == "__main__":
