# Driver program for students to try the default test cases
import random as rand
from CircularQueue import CircularQueue

def sample_test():
    """
    test for empty queue and simple enqueues
    :return: None
    """
    queue = CircularQueue()
    print(queue)
    print(f"Average: {queue.get_average()}\n")

    queue.enqueue(23)
    queue.enqueue(42)
    queue.enqueue(2)
    queue.enqueue(195)

    print(queue)
    print(f"Average: {queue.get_average()}\n")




def test_2():
    """
    test for valid resizing, should only call resize 1 time
    :return: None
    """

    queue = CircularQueue(5)


    for el in range(2, 12, 2):
        queue.enqueue(el)


    print(queue)
    print(f"Average: {queue.get_average()}\n")


    # should invoke resize only once
    for el in range(12, 22, 2):
        queue.enqueue(el)


    print(queue)
    print(f"Average: {queue.get_average()}\n")


def test_6():
    """
    Test for sequence of enqueues and dequeues and get average
    :return: None
    """

    queue = CircularQueue()

    rand.seed(10)

    # test average every 25
    # dequeue every 3 nodes
    for i in range(1, 101):
        x = rand.randint(-1000, 1000)

        queue.enqueue(x)
        queue.enqueue(x)

        if i % 25 == 0:
            print(f"Average: {queue.get_average()}\n")

        if i % 3 == 0:
            queue.dequeue()



    print(queue)
    print(f"Average: {queue.get_average()}\n")




def main():
    print("---RUNNING SAMPLE TESTCASE---")
    sample_test()

    print("---RUNNING TESTCASE #2---")
    test_2()

    print("---RUNNING TESTCASE #6---")
    test_6()

    print("---RUNNING TESTCASE #8---")
    queue = CircularQueue()
    print(queue)


    queue.enqueue(23)
    queue.enqueue(42)
    queue.enqueue(2)
    queue.enqueue(195)
    queue.enqueue(23)
    queue.enqueue(42)
    queue.enqueue(2)
    queue.enqueue(195)

    print(queue)


    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()


    print(queue)


    queue.enqueue(23)
    queue.enqueue(42)
    queue.enqueue(2)
    queue.enqueue(195)
    queue.enqueue(2)
    queue.enqueue(195)



    print(queue)

main()
