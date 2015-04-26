class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.depth = -1
        self.model = []
    def push(self,value):
        if self.root is None:
            self.root = TreeNode(value,None)
            self.depth = 0
        else:
            self.insert_value(value,self.root)
    def __str__(self):
        return str(self.model_tree(self.root,[]))
    def insert_value(self,value,parent):
        if value < parent.value:
            if parent.left is None:
                parent.left = TreeNode(value,parent)
            else:
                self.insert_value(value,parent.left)
        elif value > parent.value:
            if parent.right is None:
                parent.right = TreeNode(value,parent)
            else:
                self.insert_value(value,parent.right)
        else:
            print "invalid or duplicate value"
            return None
    def find_value(self,value,node):
        if node is None:
            return False
        if node.value == value:
            return True
        elif node.value > value:
            return self.find_value(value,node.left)
        elif node.value < value:
            return self.find_value(value,node.right)
        else:
            print 'error'

    def get_height(self,node,h=0):
        h += 1
        h1 = 0
        h2 = 0
        if node is None:
            return 0
        if node.left is not None:
            h1 = self.get_height(node.left,h)
        if node.right is not None:
            h2 = self.get_height(node.right,h)
        return max(h1,h2,h)

    def model_tree(self,node=None,model=[]):
        self.model = model
        if node is None:
            return self.model
        if node.depth > len(self.model) - 1:
            self.model.append([node.value])
        else:
            self.model[node.depth].append(node.value)
        self.model = self.model_tree(node.left,self.model)
        self.model = self.model_tree(node.right,self.model)
        return self.model

    def is_balanced(self):
        if self.root is None:
            return True
        if abs(self.get_height(self.root.left) - self.get_height(self.root.right)) < 2:
            return True
        else:
            return False
       
class TreeNode(object):
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
    def __str__(self):
        return str(self.value)
