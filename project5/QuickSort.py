from Queue import LinkedQueue, Node


def insertion_sort(queue):
  """
   Sort the the queue using insertion sort algorithm
   precondition: there is a queue which is not sorted
   postcondition: the queue is still there but its sorted now, magical isn't it
   :param val: LinkedQueue object
   :return: None
   """
  if queue.is_empty():
    return None

  if queue.head.val.isalpha():
    extra_head = Node('a', queue.head)  # This block of code keeps the queue safe between arbitrary head and tail
    queue.head = extra_head
    extra_tail = Node('z', None)
    queue.tail.next = extra_tail
    queue.tail = extra_tail

  else:
    extra_head = Node(0, queue.head)  # This block of code keeps the queue safe between arbitrary head and tail
    queue.head = extra_head
    extra_tail = Node(99, None)
    queue.tail.next = extra_tail
    queue.tail = extra_tail

  iterator_node = queue.head # initializes all the essential variable to loop through the queue
  iterator_node = iterator_node.next
  next_node_itr = iterator_node.next
  prev_node_itr = queue.head

  while iterator_node != queue.tail:

    inner_itr = queue.head # nested loop iterator

    while inner_itr != iterator_node:

      key_node = inner_itr # temp value of the inner_itr
      next_inner = key_node.next # value next to the inner_itr

      if key_node.val <= iterator_node.val < next_inner.val: # finds the position to insert element from unsorted queue to sorted queue
        key_node.next = iterator_node # this block insert the unsorted element between sorted queue
        iterator_node.next = next_inner
        prev_node_itr.next = next_node_itr
        break

      inner_itr = inner_itr.next

    prev_node_itr = iterator_node # increments the node iterator
    iterator_node = iterator_node.next
    next_node_itr = iterator_node.next

  queue.head = queue.head.next # this block gets rid of the arbitrary head and tail
  queue.tail = prev_node_itr
  queue.tail.next = None


def pick_pivot(queue):
  """
   Pick the median value between head, tail and middle to use as a pivot
   precondition: None
   postcondition: None
   :param val: LinkedQueue object
   :return: Value of a Node
   """

  head_val = queue.head.val # this block store all the values
  middle_val = queue.get_middle()
  tail_val = queue.tail.val

  if head_val > middle_val: # Breaks the problem into cases and find y for y is between x and z or (x<y<z)
    if head_val < tail_val:
      return head_val
    elif middle_val > tail_val:
      return middle_val
    else:
      return tail_val # this is the case if two values are equal
  else:
    if head_val > tail_val:
      return head_val
    elif middle_val < tail_val:
      return middle_val
    else:
      return tail_val # this is the case if two values are equal



def quick_sort(queue):
  """
   Sort the the queue using QuickSort algorithm, when the queue gets smaller than 10 during recurssion it uses insertion
   sort to sort the rest of it
   precondition: there is a queue which is not sorted
   postcondition: the queue is still there but its sorted now, magical isn't it
   :param val: LinkedQueue object
   :return: None
   """
  # everything here on down is "inspired" from Dr. Onsay's slide lecture 11 feb 15


  n = len(queue)
  if n <= 10: # calls insertion sort if elements are less than or equal to 10
    insertion_sort(queue)
    return

  p = pick_pivot(queue) # initalize less than, greater than, and equal to queues
  L = LinkedQueue()
  E = LinkedQueue()
  G = LinkedQueue()

  while not queue.is_empty():

    if queue.head.val < p:
      L.enqueue(queue.dequeue()) # creates tree of less than pivot
    elif p < queue.head.val:
      G.enqueue(queue.dequeue()) # creates tree of greater than pivot
    else:
      E.enqueue(queue.dequeue()) # creates tree of equal to pivot

  quick_sort(L) # recursive call
  quick_sort(G) # recursive call

  while not L.is_empty(): # empty out the LinkedQueues
    queue.enqueue(L.dequeue())
  while not E.is_empty(): # empty out the LinkedQueues
    queue.enqueue(E.dequeue())
  while not G.is_empty(): # empty out the LinkedQueues
    queue.enqueue(G.dequeue())
