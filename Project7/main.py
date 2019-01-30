from HashTable import HashTable, FindWords


def test01(solution):
    solution.insert("Hello", 0)
    solution.insert("Test", 1)
    solution.insert("CSE", 2)
    solution.insert("331", 3)
    solution.insert("Hash", 4)
    solution.insert("Hello", 6)
    solution.insert("World", 1)
    solution.insert("", 2)
    print(solution)
    assert(solution.tableSize == 16)
    assert(solution.numItems == 8)



def sample_test(solution):

    """
    Initial testing, it is recommended to test further.
    """

    solution.insert("Hello", 0)
    solution.insert("CSE", 2)
    solution.insert("331", 3)
    print(solution)

    # Reassigning a value
    solution.insert("Hello", 6)

    # Chaining values together
    solution.insert("1234", 123)
    solution.insert("3214", 231)

    # Test deletion
    solution.delete("World")

    # Test find
    print("Should be false: ", solution.lookup("Hey"))
    print("Should be found: ", solution.find("3214"))

    print()
    print(solution)

    # Table size should be 8, number of items should be 5
    # assert(solution.tableSize == 8)
    # assert(solution.numItems == 5)


def main():
	'''
	Main function used for testing hash table solution
	'''
	hash_table = HashTable()

	print("---TESTING HASH TABLE---")
	sample_test(hash_table)
	print("---SECOND HASH TEST---")
	test01(hash_table)


	# Test Find Words
	phrase = "abcdaba"
	print()
	print("---TESTING FIND WORDS---")
	test_list = FindWords(phrase, 2)
	print("Words appearing twice: ", test_list)
	print("Words appearing 3 times: ", FindWords(phrase, 3))
	print()

if __name__ == "__main__":
	main()