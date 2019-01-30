########################################
# PROJECT 6 - BinarySearchTree
# Author: Daewoo Maurya
# PID: A54642636
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Describes equality comparison for nodes ('==')
        :param other: node being compare to
        :return: True if equal, False if not equal
        """
        return type(other) is type(self) and self.value == other.value

    def __repr__(self):
        """
        Defines string representation of a node (str())
        :return: string representing node
        """
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        :return nothing
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result


    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        insert a value to the Binary Search Tree
        :param value: Value to be inserted in the BST
        :return: None
        """
        if self.root is None:
            self.root = Node(value)  # empty tree case

        pos = self.search(value, self.root)
        if pos.value < value:  # left insert in the tree
            pos.right = Node(value, pos)
        elif pos.value > value:  # right insert in the tree
            pos.left = Node(value, pos)

        self.size += 1  # increment the size

    def remove(self, value):
        """
        Finds the value to be deleted in the BinarySearchTree, remove the value from the tree and make appropriate changes to the tree
        :param value: Value to be deleted
        :return: The deleted value
        """
        node = self.search(value, self.root)

        if node:

            if node.left is None and node.right is None:  # leaf node case
                parent = node.parent
                if parent.left is node:
                    parent.left = None
                elif parent.right is node:
                    parent.right = None

            elif node.left is not None and node.right is None:  # node with only left child
                parent = node.parent
                parent.left = node.left
            elif node.left is None and node.right is not None:  # node with only right child
                parent = node.parent
                parent.right = node.right
            elif node.left is not None and node.right is not None:  # node with both left and right child
                min_right_node = self.min(node.right)
                min_right_node_parent = min_right_node.parent
                node.value = min_right_node.value

                min_right_node_parent.left = None


            self.size -= 1  # decrement size for the deleted
            return Node

    def search(self, value, node):
        """
        Search for a node in the Binary Search Tree
        :param value: Search Value
        :param node: Recursive Node
        :return: The node position
        """
        if self.root is None:  # empty tree
            return None
        if node.value == value:  # value found
            return node
        elif value < node.value and node.left is not None:
            return self.search(value, node.left)  # recursive left call
        elif value > node.value and node.right is not None:
            return self.search(value, node.right)  # recursive right call
        return node


    def inorder(self, node, inorder_list=list()):
        """
        Stores the values of a binary search tree in list as inorder form
        :param node: Recursive Node, starts with root
        :param inorder_list: Stores the values in a BST
        :return: the inorder list
        """

        if node.left is not None:
            self.inorder(node.left, inorder_list)  # left child recursive call

        inorder_list.append(node.value)  # make inorder list

        if node.right is not None:
            self.inorder(node.right, inorder_list)  # right child recursive call

        return inorder_list




    def preorder(self, node, preorder_list=list()):
        """
        Stores the values of a binary search tree in list as preorder traversal form
        :param node: Recursive Node, starts with root
        :param preorder_list: Stores the values in a BST
        :return: the preorder_list
        """
        if node is not None:
            preorder_list.append(node.value)  # make preorder list
            self.preorder(node.left, preorder_list)  # left child recursive call
            self.preorder(node.right, preorder_list)  # right child recursive call

        return preorder_list



    def postorder(self, node, postorder_list=list()):
        """
        Stores the values of a binary search tree in list as postorder traversal form
        :param node: Recursive Node, starts with root
        :param postorder_list: Stores the values in a BST
        :return: the postorder_list
        """

        if node:
            self.postorder(node.left, postorder_list)  # left child recursive call
            self.postorder(node.right, postorder_list)  # right child recursive call
            postorder_list.append(node.value)  # make postorder list
        return postorder_list

    def depth(self, value):
        """
        finds the value in a BinarySearchTree, it the value exist finds the depth of a node with the value
        :param value: value to look for in the BST
        :return: the Depth of the value in the BST
        """
        pos = self.search(value, self.root)  # look for the value of which depth is required
        depth = 0
        if pos.value != value:  # value not found in the tree
            return -1
        while pos is not None:  # find the number of ancestors
            pos = pos.parent
            depth += 1

        return depth - 1

    def height(self, node):
        """
        finds the height of a BinarySearchTree
        :param node: recursive node
        :return: The height of the tree
        """
        if self.root is None:
            return 0

        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))  # find the max number of children in left OR right child


    def min(self, node):
        """
        Finds the minimun value in a BinarySearchTree
        :param node: recursive Node
        :return: The minimum value in a BinarySearchTree
        """

        if self.root is None:  # empty tree
            return None
        min_node = node  # initial comparison node
        if node is not None and node.left is not None:  # leftest node will be the smallest node
            min_node = self.min(node.left)
        return min_node

    def max(self, node):
        """
        Finds the maximum value in a BinarySearchTree
        :param node: recursive Node
        :return: The maximum value in the tree
        """

        if self.root is None:
            return None
        max_node = node  # initial max comparison node
        if node is not None and node.right is not None:  # rightest node will be the smallest node
            max_node = self.max(node.right)
        return max_node

    def get_size(self):
        """
        finds size of the binary Search tree
        :return: Size of BST
        """
        return self.size  # returns the size of the tree
