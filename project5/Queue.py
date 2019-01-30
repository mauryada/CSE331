class Node:
  """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

  __slots__ = 'val', 'next'         # streamline memory usage

  def __init__(self, val, next):
    self.val = val
    self.next = next

  def __lt__(self, other):
    ''' assumes other is of same type, invoked with "<" '''
    return self.val <= other.val

  def __le__(self, other):
    ''' assumes other is of same type, invoked with "<=" '''
    return self.val <= other.val



class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  def __init__(self):
    """Create an empty queue."""
    self.head = None
    self.tail = None
    self.size = 0


  def __str__(self):
    ''' string implementation of current elements in queue '''
    head = self.head
    values = list()
    while head:
      values.append(str(head.val))
      head = head.next

    return ", ".join(values)

  __repr__ = __str__


################## start modifying below this line ######################

  ###################################
  # PROJECT 5 - Queue
  # Author: Daewoo Maurya
  # PID: A54642636
  ###################################

  def __len__(self):
    """
    Finds the length of the of the queue
    precondition: None
    postcondition: None
    :param val: self object
    :return: Length of the queu
    """
    return self.size

  def is_empty(self):
    """
    Checks if the queue is empty
    precondition: None
    postcondition: None
    :param val: self object
    :return: Bool value, empty of not empty
    """
    return not self.head

  def dequeue(self):
    """
    Removes the element from the class object according to queue based ADT object
    precondition: there is a queue
    postcondition: the head of the queue is gone now
    :param val: self object
    :return: deleted value in the head
    """
    if self.is_empty():
      return None # empty case
    else:
      deleted_val = self.head.val # store value
      self.head = self.head.next # increments head
      self.size -= 1 # decrease size
      return deleted_val # return value

  def enqueue(self, element):
    """
    Adds the element to the class object according to queue based ADT object
    precondition: there is a queue
    postcondition: there is queue with one more element at the end
    :param val: self object, element to be inserted
    :return: None
    """
    new_node = Node(element, None) # new node to be added

    if self.is_empty(): # empty queue case
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.next = new_node # adds element at the end
      self.tail = new_node # changes tail

    self.size += 1 # increase size


  def get_middle(self):
    """
    gets the middle value of the queue
    precondition: there is a queue
    postcondition: there is still a queue
    :param val: self object
    :return: value of the middle element in the queue
    """
    if not self.is_empty():
      temp_self = self.head
      i = 0
      while temp_self is not None and i <= self.size//2: # gets the value at index size//2
        i+=1
        temp_self = temp_self.next # moves on the node iterator
      return temp_self.val


