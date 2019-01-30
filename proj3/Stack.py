###################################
# PROJECT 3 - STACK
# Author: Daewoo Maurya
# PID: A54642636
###################################

class Stack:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, capacity=2):
        """
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack.
        """
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._size = 0

    def __str__(self):
        """
        Prints the elements in the stack from bottom of the stack to top,
        followed by the capacity.
        :return: string
        """
        if self._size == 0:
            return "Empty Stack"

        output = []
        for i in range(self._size):
            output.append(str(self._data[i]))
        return "{} Capacity: {}".format(output, str(self._capacity))

    ###### COMPLETE THE FUNCTIONS BELOW ######

    # --------------------Accessor Functions---------------------------------
    def get_size(self):
        """Returns the size of the Stack object
            return: int
        """
        return self._size

    def is_empty(self):
        """Returns the boolean value of whether the stack is empty or not
           Return: Bool
        """
        return self._size == 0

    def top(self):
        """Return the value at the top of the stack
            Return: Element of the data in stack
        """
        if self.is_empty():
            return None
        else:
            return self._data[self._size-1]

    # ---------------------------Mutator Functions------------------------------

    def push(self, addition):
        """Add value to the stack
            Return: None
        """
        if self._size == self._capacity: #case to grow the list
            self.grow()
            self._data[self._size] = addition
            self._size+=1 # adds size to add element
        else:
            self._data[self._size] = addition
            self._size += 1


    def pop(self):
        """Remove the value from the top of the stack and returns the removed value, returns none if stack is empty
           return: Last element of the stack or None if stack is empty
        """
        if self.is_empty():
            return None

        if self._size <= self._capacity//2 and self._capacity//2 > 2: # prevents the caoacity from being reduced to less than 2 and checks it size is less that or equal to half the capacity
            self.shrink()
        return_popped = self._data[self._size-1] # return value
        self._data[self._size-1] = 0 # change the value of the removed element to default 0
        self._size -= 1 # removes reference to the last element
        return return_popped

    def grow(self):
        """Increase the capacity of the stack and creates a new list with increased capacity"""
        if not self._capacity:
            self.__init__()
            return

        new_data = [0] * 2 * self._capacity # creates new data to be added to the Stack object _data
        for i in range(self._capacity):
            new_data[i] = self._data[i] # adds old data to new list
        self._capacity *= 2 # increments the capacity
        self._data = new_data

    def shrink(self):
        """Shrink the capactiy of the stack to half if there is empty space
            Return: None
        """
        self._capacity = self._capacity // 2
        self._data = self._data[:self._capacity]


def Palindrome(phrase):
    '''
    Checks if a string is a palindrome using stack. Ignores punctuations and capitalization in the string
    Return: Bool
    '''
    phrase = phrase.lower()
    new_phrase = ""
    palinStack = Stack()

    for ch in phrase:
        if ch.isalnum():
            new_phrase += ch # creates new sting without punctuations
            palinStack.push(ch)

    palinStackCheck = ""
    while not palinStack.is_empty():
        palinStackCheck += palinStack.pop() # creates string with the elements popped from the string using stack concepts

    return palinStackCheck == new_phrase # checks if stack popped string is same as string without