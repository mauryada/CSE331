###################################
# PROJECT X - QUEUE
# Author:
# PID:
###################################

class ArrayQueue:
    def __init__(self,capacity=1):
        """Create an empty queue."""
        self._capacity = capacity
        self._data = [None]*self._capacity
        self._size = 0
        self._front = 0

    def __str__(self):
        """
        Prints the elements in the queue from last of the queue to first,
        followed by the capacity.
        :return: string
        """
        if self._size == 0:
            return "Empty Queue"

        output = []
        for i in range(self._size):
            output.append(str(self._data[i+self._front]))
        return "{} Capacity: {}".format(output, str(self._capacity))

    ###### COMPLETE THE FUNCTIONS BELOW ######

    # --------------------Accessor Functions---------------------------------

    def get_size(self):
        """"Returns number of items currently in the queue"""
        return self._size

    def is_empty(self):
        """"Returns True if the queue is empty, False if not"""
        if self._size == 0:
            return True
        else:
            return False

    def first(self):
        """"Returns but does not remove, the first item from the queue"""
        if self.is_empty():
            return None
        else:
            return self._data[self._front]

    # ---------------------------Mutator Functions------------------------------

    def dequeue(self):
        """Remove and return the first element of the queue or None if the queue is empty."""
        if self.is_empty():
            return None
        output = self.first()
        self._data[self._front] = None

        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        self.resize()
        return output

    def enqueue(self, e):
        """Add an item to the back of queue."""
        self.resize()
        avail = (self._front + self._size) % self._capacity
        self._data[avail] = e
        self._size += 1

    def resize(self):
        """Resize the queue to be half its current capacity when queue size is less than or equal to half its capacity,
            or resize the queue to be be 2 times its previous size when queue size equals capacity"""
        new_capacity=self._capacity
        if 0 < self._size <= self._capacity // 2: # if queue size is not empty and less than half or equal to its capacity
            new_capacity = self._capacity // 2 # new_capacity shrink to half of its current capacity
        elif self._size == self._capacity: # if queue size equal to its current capacity
            new_capacity = 2 * self._capacity # new_capacity growths to twice of its current capacity

        old = self._data # make a copy of current data
        self._data = [None] * new_capacity #allocate list with new capacity
        beginning = self._front
        for k in range(self._size):
            self._data[k] = old[k+beginning] # only consider existing elements

        self._capacity = new_capacity # current capacity is new capacity
        self._front = 0  # front has been initialized