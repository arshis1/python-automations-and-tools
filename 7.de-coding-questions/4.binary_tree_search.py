##########################################
#Binary Search Tree Check
#Given a binary tree, check whether it’s a binary search tree or not
###########################################

class Node:

    def __init__(self, value):
        self.value = value
        self.lnode = None 
        self.rnode = None 
    
    def insert(self,value):
        if value > self.value:
            if self.rnode is None:
                print("Right Node Not Found: Inserting ", value)
                self.rnode = Node(value)
            else:
                #recurssion
                print("Traversing Right tree for", value)
                self.rnode.insert(value)
        else:
            if self.lnode is None:
                print("Left Node Not Found: Inserting ", value)
                self.lnode = Node(value)
            else:
                #recussion
                print("Traversing Left tree for", value)
                self.lnode.insert(value)


if __name__ == "__main__":
    lst = [10,5,15,3,7,12,18]
    root = None

    for input in lst:
        if root is None:
            print("RRoot Node Not Found: Inserting ", input)
            root = Node(input)
        else:
            root.insert(input)

