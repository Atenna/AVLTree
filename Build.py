__author__ = 'Carmen'
import sys
import AVLTree


def main():
    tree = AVLTree.AVLTree()
    nodes = (5, 3, 7, 10, 11)
    print('Inserting nodes', nodes)
    for key in nodes:
        tree.insert(key)
        print(key)

    print(tree.inorder())

if __name__ == "__main__":
    main()