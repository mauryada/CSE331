from BinarySearchTree import BinarySearchTree, Node

# MAKE CHANGES AND DO YOUR OWN TESTING - this file is not submitted


def test1(bst):
    """
    tests insert, traversals, and height
    :param bst: binary search tree
    :return: None
    """
    bst.insert(5)
    bst.insert(9)
    bst.insert(4)
    bst.insert(12)
    bst.insert(7)
    bst.insert(2)

    print("-----TEST 1-----")
    print("In-order:   ", bst.inorder(bst.root, []))
    print("Pre-order:  ", bst.preorder(bst.root, []))
    print("Post-order: ", bst.postorder(bst.root, []))
    print("Root:       ", bst.root)
    print("Height:     ", bst.height(bst.root), "\n")
#
def test2(bst):
    """
    tests insert, part of remove
    :param bst: binary search tree
    :return: None
    """
    bst.insert(8)
    bst.insert(3)
    bst.remove(12)  # Remove a leaf

    print("-----TEST 2-----")
    print("In-order:   ", bst.inorder(bst.root, []))
    print("Root:       ", bst.root, "\n")

def test3(bst):
    """
    tests insert, part of remove
    :param bst: binary search tree
    :return: None
    """
    print("-----TEST 3-----")
    print()
    print("1 In-order:   ", bst.inorder(bst.root, []))
    bst.insert(6)
    print("2 In-order:   ", bst.inorder(bst.root, []))
    bst.remove(5)  # Remove the root
    print("3 In-order:   ", bst.inorder(bst.root, []))
    bst.remove(4)  # Remove with one child
    print("4 In-order:   ", bst.inorder(bst.root, []))

    print("-----TEST 3-----")
    print("In-order:   ", bst.inorder(bst.root, []))
    print("Pre-order:  ", bst.preorder(bst.root, []))
    print("Post-order: ", bst.postorder(bst.root, []))
    print("Root:       ", bst.root)
    print("Height:     ", bst.height(bst.root), "\n")

def test4(bst):
    """
    tests depth, height, min, max, and get_size
    :param bst: binary search tree
    :return: None
    """
    print("-----TEST 4-----")
    print("Depth(8):   ", bst.depth(8))
    print("Depth(6):   ", bst.depth(6))
    print("Depth(1):   ", bst.depth(1))
    print("Height:     ", bst.height(bst.root))
    print("Min:        ", bst.min(bst.root))
    print("Max:        ", bst.max(bst.root))
    print("Size:       ", bst.get_size())


def main():
    bst = BinarySearchTree()
    test1(bst)
    test2(bst)
    test3(bst)
    test4(bst)


main()
