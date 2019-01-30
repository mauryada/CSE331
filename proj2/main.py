from MergeSort import *
import sys


def AddValues(list_, fp):
    '''
    :param list_: linked list to add values to
    :param fp: file pointer to read from
    :return:  None
    '''
    for num in fp:
        list_.push_back( float(num))




if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    list_ = LinkedList()

    AddValues(list_, fp)
    list_.head = MergeSort(list_.head)
    print(list_)
    fp.close()