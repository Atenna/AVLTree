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
            print("INSERTING NODE ", key, " AS LEAF")
            self.node = newNode
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < root.key:
            print("INSERTING NODE ", key, " TO LEFT from ", self.node.key)
            root.left.insert(key)

        elif key > root.key:
            print("INSERTING NODE ", key, " TO RIGHT from", self.node.key)
            root.right.insert(key)

        # else: key is already in the tree

        self.rebalance()

    def rebalance(self):
        # update height of this ancestor node___?
        self.updateHeight()
        self.updateBalance()
        #While the tree is not balanced
        while self.balance > 1 or self.balance < -1:
            # Left subtree > Right subtree
            if self.balance > 1:
                # Left-Right Case
                #      o
                #     / \
                #   o    o
                #  / \      => left rotation
                # o   o
                #    / \
                #   o   o
                if self.node.left.balance < 0:
                    print("LEFT subtree > RIGHT -> LEFT ROTATION")
                    self.leftRotate(self.node.left)
                    self.updateHeight()
                    self.updateBalance()
                # Left-Left Case => right rotation
                self.rightRotate(self.node.left)
                self.updateHeight()
                self.updateBalance()
            # Left subtree > Right subtree
            if self.balance < -1:
                # Right-Left Case
                if self.node.right.balance > 0:
                    print("LEFT subtree < RIGHT -> RIGHT ROTATION")
                #      o
                #     / \
                #   o    o
                #       / \      => right rotation
                #      o   o
                #    / \
                #   o   o
                    self.rightRotate(self.node.right)
                    self.updateHeight()
                    self.updateBalance()
                self.leftRotate(self.node.right)
                self.node.updateHeight()
                self.node.updateBalance()
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
        print("LEFT ROTATION")
        #Right Right Case #Right Left Case
        y = x.right
        p = y.left
        #rotation
        x.right = p
        y.left = x
        #update heights
        y.height = max(y.left.height, y.right.height)+1
        x.height = max(x.left.height, x.right.height)+1

    def updateHeight(self):

        # Height of the tree is max height of either left or right subtree +1
        if self.node:
            if self.node.left:
                self.node.left.updateHeight()
            if self.node.right:
                self.node.right.updateHeight()
# TO DO, ROTATION, REBALANCING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            self.node.height = max(self.node.right.height,self.node.left.height) + 1
            print("UPDATING HEIGHT OF NODE ", self.node.key, " WITH ", self.node.height)
        else:
            # root
            self.height = -1

    def updateBalance(self):
        if self.node:
            if self.node.left:
                self.node.left.updateBalance()
            if self.node.right:
                self.node.right.updateBalance()
            # Balance = Height of Left - Height of Right node
            self.balance = self.node.left.height = self.node.right.height
        else:
            # root
            self.balance = 0

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
