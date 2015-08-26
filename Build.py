__author__ = 'Carmen'
import sys
import AVLTree

def main():
    tree = AVLTree()
    nodes = [5, 3, 7, 10, 11]
    sys.stdout('Inserting nodes', nodes)
    for key in nodes:
        tree.insert(key)

    tree.inorder()
    sys.stdout(tree.result())

if __name__ == "__main__":
    main()