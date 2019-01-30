
class LinkedListNode:
    def __init__(self, val = None):
        """
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.val = val
        self.next = None

    def __le__(self, other):
        '''
        :param other: Linked list node
        :return: boolean value of less than equal to other
        '''
        if isinstance(other, LinkedListNode):
            return self.val <= other.val





class LinkedList:
    def __init__(self):
        """
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None

    def __repr__(self):
        '''
        :param: none
        :return: string representation of linked list
        '''
        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    __str__ = __repr__


    def push_back(self, data):
        '''
        :param data:  val for new node to be added to Linked list
        :return: None
        '''
        node = LinkedListNode(data)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = node

        else:
            self.head = node




'''
ANYTHING BEFORE THIS COMMENT SHOULDN'T BE MODIFIED IN ANYWAY!
'''
# --------- START MODIFYING HERE ---------


def listSize(head):
    """Return the size of the linked list"""
    current = head
    count = 0
    while current:
        count+=1 # count of elements
        current = current.next
    return count


def split(head):
    """Split the linked list in half for even number of elements and with one extra element more element """

    list_size = listSize(head)

    left_list = LinkedList()
    right_list = LinkedList()

    if list_size < 2: #single element case
        return (head, None)


    if list_size%2: #case for odd number of elements
        mid = (list_size+1)/2
    else: #case for even number of elements
        mid = list_size/2

    next_node = head
    counter = 0
    while next_node:

        if counter< mid: #left list
            left_list.push_back(next_node.val)
        else: #right list
            right_list.push_back(next_node.val)

        next_node = next_node.next
        counter+=1 #counter to keep under mid for leftlist

    return left_list.head, right_list.head


def merge(left_list, right_list):
    """Merge the two sorted linked list into one sorted linked list"""

    merged_list = LinkedList()

    while left_list and right_list:

        if left_list.val >= right_list.val: #put the value into merged list in a sorted manner
            merged_list.push_back(right_list.val)
            right_list = right_list.next
        elif left_list.val < right_list.val:
            merged_list.push_back(left_list.val)
            left_list = left_list.next

    while left_list:# left out elements
        merged_list.push_back(left_list.val)
        left_list = left_list.next
    while right_list:# left out elements
        merged_list.push_back(right_list.val)
        right_list = right_list.next

    return merged_list.head


def MergeSort(head):
    """Uses merge sort algorithm to sort a linked list using recursion"""

    if head is None or head.next is None:
        return head

    left_list, right_list = split(head)

    left_list = MergeSort(left_list)
    right_list = MergeSort(right_list)

    return merge(left_list, right_list)


