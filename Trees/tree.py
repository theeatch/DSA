class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if self.value == value:
            return
        
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinaryTree(value)

        if value > self.value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinaryTree(value)

    def inOrder(self):
        resultArr = []

        if self.left:
            resultArr += self.left.inOrder()

        resultArr.append(self.value)

        if self.right:
            resultArr += self.right.inOrder()

        return resultArr
    

    def searchElement(self, element):
        if element == self.value:
            return True
        
        if element < self.value:
            if self.left:
                return self.left.searchElement(element)
            else:
                return False
            
        if element > self.value:
            if self.right:
                return self.right.searchElement(element)
            else:
                return False
            
        return False
    
def BuildTree(eleArray):
    root = BinaryTree(eleArray[0])

    for i in range(1, len(eleArray)):
        root.insert(eleArray[i])
        
    return root
    
if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    myTree = BuildTree(numbers)
    print(myTree.inOrder())
    print("Number 19 exists in tree? ", myTree.searchElement(19))
