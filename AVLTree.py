__author__ = 'Carmen'
import Node

class AVLTree:

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if not self.node:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        # else: key is already in the 3

        self.rebalance()

    def rebalance(self):

