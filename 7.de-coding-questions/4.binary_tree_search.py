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
                print("Right note is not empty and value " ,value, "is greater than surrent right node value:" ,self.value)
                print("Traversing Right tree for", value)
                self.rnode.insert(value)
        else:
            if self.lnode is None:
                print("Left Node Not Found: Inserting ", value)
                self.lnode = Node(value)
            else:
                #recussion
                print("Left note is not empty and value " ,value, "is less than surrent left node value:" ,self.value)
                print("Traversing Left tree for", value)
                self.lnode.insert(value)



if __name__ == "__main__":
    #create a binary tree:
    lst = [10,5,15,3,7,12,18]
    new_lst = sorted(lst)
    print(new_lst)
    root = None

    for input in new_lst:
        if root is None:
            print("RRoot Node Not Found: Inserting ", input)
            root = Node(input)
        else:
            root.insert(input)

    #find in the binary tree:

    #is binary search tree:


