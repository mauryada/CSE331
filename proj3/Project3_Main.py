import sys
from Stack import Stack
from Stack import Palindrome

def AddValues(list_, fp):
    '''
    :param list_: linked list to add values to
    :param fp: file pointer to read from
    :return:  None
    '''
    for num in fp:
        list_.push(int(num))

def main():
    print("-----TEST 1-----")
    # fp = open(input("Please Enter File Name: "), "r")
    # mystack = Stack()
    # AddValues(mystack, fp)

    stack1 = Stack()
    stack1.push(2)
    print(stack1)
    stack1.pop()
    print(stack1)
    stack1.push(4)
    print(stack1)
    stack1.push(8)
    print("Top: " + str(stack1.top()))
    stack1.push(5)
    print("Top: " + str(stack1.top()))

    stack1.pop()
    stack1.push(6)
    print(stack1)
    stack1.pop()
    stack1.pop()
    stack1.push(7)
    print(stack1)

    print("\n-----TEST 2-----")
    stack2 = Stack()
    stack2.push(2)
    stack2.push(5)
    stack2.push(14)
    stack2.push(7)
    stack2.push(3)
    stack2.push(7)
    print(stack2)
    stack2.push(89)
    stack2.push(23)
    stack2.push(7)
    print(stack2)
    stack2.pop()
    stack2.pop()
    print(stack2)
    stack2.push(8)
    stack2.push(9)
    print(stack2)
    print("Top: " + str(stack2.top()))
    stack2.push(15)
    stack2.push(3)
    stack2.push(7)
    stack2.push(8)
    print("Top: " + str(stack2.top()))
    stack2.push(45)
    print(stack2)
    stack2.push(34)
    stack2.push(2)
    stack2.push(5)
    print("Top: " + str(stack2.top()))
    stack2.push(9)
    print("Top: " + str(stack2.top()))
    print(stack2)

    print("\n-----TEST 3-----")
    print(Palindrome("Racecar"))
    print(Palindrome("Kayak"))
    print(Palindrome("tkujg"))
    print(Palindrome("Eva, can I see bees in a cave?"))
    print(Palindrome("I did, did I?"))


main()