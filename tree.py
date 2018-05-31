class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.value)

class BinarySearchTree():
    def __init__(self,value):
        self.root = TreeNode(value)

    def __repr__(self):
        ptr = self.root
        res = []
        self.inOrderTraversal(ptr,res)
        return ",".join(res)

    def inOrderTraversal(self,root,res):
        if root:
            self.inOrderTraversal(root.left,res)
            res.append(str(root.value))
            self.inOrderTraversal(root.right,res)

    def preOrderTraversal(self,root,res):
        if root:
            res.append(str(root.value))
            self.preOrderTraversal(root.left,res)
            self.preOrderTraversal(root.right,res)

    def postOrderTraversal(self,root,res):
        if root:
            self.preOrderTraversal(root.left,res)
            self.preOrderTraversal(root.right,res)
            res.append(str(root.value))

    def add(self,value):
        ptr = self.root
        while ptr:
            if value >= ptr.value:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = TreeNode(value)
                    return
            else:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = TreeNode(value)
                    return
    
    def contains(self,value):
        ptr = self.root
        while ptr:
            if ptr.value == value:
                return True
            elif value > ptr.value:
                ptr = ptr.right
            else:
                ptr = ptr.left
        return False
    
    def remove(self,value):
        ptr = self.root
        while ptr:
            if ptr.value == value:
                if ptr.left and not ptr.right:
                    ptr = ptr.left
                elif ptr.right and not ptr.left:   
                    ptr = ptr.right
                elif ptr.left and ptr.right:
                    ptr2 = ptr.right
                    while ptr2.left:
                        ptr2 = ptr2.left
                    ptr2.value, ptr.value = ptr.value, ptr2.value
                    if ptr.right.value == value:
                        ptr.rgiht = None
                    else:
                        ptr = ptr.right
                        while ptr.left and ptr.left.value != value:
                            ptr = ptr.left
                        ptr.left = None
                else:
                    ptr = None
            elif value > ptr.value:
                ptr = ptr.right
            else:
                ptr = ptr.left
        return False

#Test Remove
a = BinarySearchTree(10)
a.add(15)
a.add(13)
a.add(20)
a.add(19)
a.add(18)
print(a)
a.remove(15)
print(a)
