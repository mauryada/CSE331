###################################
# PROJECT 4 - CircularQueue
# Author: Daewoo Maurya
# PID: A54642636
###################################

class CircularQueue(object):
    def __init__(self, capacity=2):
        """
        Initialize the queue to be empty with a fixed capacity
        :param capacity: Initial size of the queue
        """

        self.capacity = capacity
        self.size = 0
        self.list = [0] * self.capacity
        self.sum = 0
        self.read = 0
        self.write = 0

    def __eq__(self, other):
        return self.capacity == other.capacity \
               and self.size == other.size \
               and self.read == other.read \
               and self.write == other.write

    # ----------------------- MODIFY BELOW THIS LINE ---------------------------
    def __str__(self):
        """
        String representation of the queue, and the string representation rotates according to the read and write
        :return: string of value
        """

        if self.size == 0:
            return "Queue is empty"

        content = ""
        ##  INSERT STRING OUTPUT CODE HERE!

        content += str(self.list[(0 + self.read)])
        for i in range(1, self.size):
            content += ", " + str(self.list[(i+self.read) % self.capacity]) #adds elements as string and rotate around the queue as well

        return f"Contents: {content}"


    # DO NOT MODIFY or DELETE this line
    __repr__ = __str__

    def enqueue(self, number):
        """
        Adds the value 'number' to the queue based class
        :param val: Number to add
        :return: No return
        """
        if self.size == self.capacity:  # full queue
            self.resize()  # increase capacity by 2 times

        self.write = (self.read + self.size) % self.capacity  # changes write value to the next index
        self.list[self.write] = number  # add number to the queue
        self.size += 1
        self.sum += number  # adds sum of the number added

    def dequeue(self):
        """
        Removes the element from the class object according to queue based ADT object
        :param val: self object
        :return: No return
        """
        if self.size == 0:  # doesn't do anything if queue is empty
            return None

        self.sum -= self.list[self.read]  # decrease the sum by the deleted element
        self.list[self.read] = 0  # reassign arbitrary value to the index to delete value
        self.read = (self.read + 1) % self.capacity  # increase the front index
        self.size -= 1  # change size


    def resize(self):
        """
        increase the capacity by 2 times to accommodate new data entry in the queue
        :param val: self object
        :return: No return
        """
        new_list = [0]*2*self.capacity  # new list with twice the capacity

        for i in range(self.capacity):
            new_list[i] = self.list[(i+self.read) % self.capacity]  # adds all the values to the new list

        self.list = new_list  # change all the values in the object
        self.read = 0
        self.write = self.size-1
        self.capacity *= 2



    def get_average(self):
        """
        calculate the average of the values present in the queue
        :param val: self object
        :return: average of the elements in queue
        """
        if self.size == 0:
            return 0
        else:
            return self.sum / self.size  # calculate the average

