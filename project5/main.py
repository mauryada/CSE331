#!/usr/bin/python3
from QuickSort import quick_sort, insertion_sort
from Queue import LinkedQueue


def AddValues(queue, L, fp):
    '''
    :param queue: queue to add values to
    :param fp: file pointer to read from
    :return:  None
    '''
    for line in fp:
        line = line.split()

        for num in line:
            queue.enqueue((num))
            L.append((num.strip()))


if __name__ == '__main__':
    # fp = open(input("Please Enter File Name: "), "r")
    fp = open("test8.txt", 'r')
    # fp = open("test3.txt", 'r')
    q = LinkedQueue()
    L = []
    AddValues(q, L, fp)
    print(q.__len__())

    fp.close()
    print(q, "unsorted")
    print()
    # insertion_sort(q)
    quick_sort(q)
    print(q, "sorted")

    S = ""
    L = sorted(L)
    for i in L:
        S += str(i) + ", "
    S = S[:-2]
    print(S)
    print(q)
    print(str(q) == S)
