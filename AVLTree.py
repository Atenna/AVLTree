__author__ = 'Carmen'


class Node(object):
    def __init__(self, key):
        """
        Node constructor
        """
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

    def __str__(self):
        return "%s" % self.key


class AVLTree(object):

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        root = self.node
        newNode = Node(key)

        if not root:
            root = newNode
            root.left = AVLTree()
            root.right = AVLTree()

        elif key < root.key:
            root.left.insert(key)

        elif key > root.key:
            root.right.insert(key)

        # else: key is already in the tree

        self.rebalance()

    def rebalance(self):
        # update height of this ancestor node
        None
        #to-do

    def rightRotate(y):
        #Left Left Case #Left Right Case
        x = y.left
        p = x.right
       # rotations
        x.right = y
        y.left = p
        #update heights
        y.height = max(y.left.height, y.right.height)+1
        x.height = max(x.left.height, x.right.height)+1

    def leftRotate(x):
        #Right Right Case #Right Left Case
        y = x.right
        p = y.left
        #rotation
        x.right = p
        y.left = x
        #update heights
        y.height = max(y.left.height, y.right.height)+1
        x.height = max(x.left.height, x.right.height)+1

    def getBalanceFactor(node):
        if node is None:
            return 0
        return (node.left.height - node.right.height)

    def inorder(self):
        result = []

        if not self.node:
            return result
        result.extend(self.node.left.inorder())
        result.append(self.node.key)
        result.extend(self.node.right.inorder())

        return result

if __name__ == '__main__':
        tree = AVLTree()
        nodes = [5, 3, 7, 10, 11]
        print('Inserting nodes', nodes)
        for key in nodes:
            tree.insert(key)

        print(tree.inorder())
