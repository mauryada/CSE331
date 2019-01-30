class HashListNode:
    def __init__(self, key, val = None):
        """
        DO NOT EDIT
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.value = val
        self.key = key
        self.next = None

    def __str__(self):
        '''
        DO NOT EDIT
        String representation of a linked list node

        :return: String representation
        '''
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        '''
        DO NOT EDIT
        Equality operator
        :return: True if equal, false if not
        '''

        if self and other:
            return self.value == other.value and self.next == other.next \
                   and self.key == other.key
        elif not self and not other:
            return True

        return False

class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None
        self.tail = None

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """

        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next
                temp_other = temp_other.next
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True


    # -------------------------------
    # ----- DO NOT MODIFY ABOVE -----
    # ----- MODIFY BELOW ------------
    # -------------------------------


    def __repr__(self):
        """
        String representation of the linkedList class
        :return: output string
        """

        temp_node = self.head
        if temp_node is None:
            return ""
        output = ""
        while temp_node is not None:
            output += "{}:{} -> ".format(temp_node.key, temp_node.value)
            temp_node = temp_node.next
        return output[:-4]


    __str__ = __repr__


    def append(self, key, value):
        """
        Adds HashNode to the end of the linked list, HashNode contains key and Value
        :param key: Key string
        :param value: Value corresponding to the key
        :return: None
        """

        new_node = HashListNode(key,value)  # new node to be added to the list
        if self.head == None:
            self.head = new_node
            self.tail = new_node  # updates all the values accordingly
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, key):
        """
        Removes a HashNode from the LinkedList if the key of the Node is same as the key in the parameter
        :param key: The node to be deleted
        :return: None
        """

        if self.head.key == key:
            self.head = self.head.next  # first node to be removed case
            self.tail = None
            return

        temp_self = self.head
        while temp_self.next is not None:  # temp_self.next because its a singly linked list
            if temp_self.next.key == key:  # finds the key
                if self.tail.key == key:
                    self.tail = temp_self.next  # updates tail if tail is removed
                temp_self.next = temp_self.next.next
                return
            temp_self = temp_self.next

    def find(self, key):
        """
        Finds a key in the list and return the node
        :param key: Key that needs to be found
        :return: HashNode with the required key
        """
        if self.head is None:
            return False
        temp_self = self.head
        while temp_self is not None:
            if temp_self.key == key:  # finds the key in the linked list
                return temp_self
            temp_self = temp_self.next
        return False
