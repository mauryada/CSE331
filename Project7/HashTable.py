from LinkedList import LinkedList, HashListNode


class HashTable:
    """
    Hash table class, utilizes linked list for resolving collisions with separate chaining
    """
    def __init__(self, tableSize=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.tableSize = tableSize
        self.numItems = 0
        self.table = [LinkedList() for i in range(self.tableSize)]

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.tableSize != other.tableSize:
            return False
        for i in range(self.tableSize):
            if self.table[i] != other.table[i]:
                return False
        return True

    def hash_function(self, x):
        """
        DO NOT EDIT
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.tableSize


    # ------------------------------------------
    # ---------- DO NOT MODIFY ABOVE -----------
    # ------------------------------------------
    # -------------- MODIFY BELOW --------------


    def __repr__(self):
        """
        String representation of the HashTable class
        :return: output string
        """
        output = ""
        for i in range(self.tableSize):
            output += "[{}]: {} \n".format(i, self.table[i])
        return output

    __str__ = __repr__

    def insert(self, key, value):
        """
        Add a Node with key and value to the HashTable ADT
        :param key: Key for the hash
        :param value: Value for the corresponding key
        :return: None
        """
        if key is None or key == '':
            return None

        loc_index = self.hash_function(key)  # index in hash corresponding to the string

        key_exist = self.table[loc_index].find(key)
        if key_exist:
            key_exist.value = value  # updates value if key exist
            return

        self.table[loc_index].append(key, value)  # adds the key and value to the proper index
        self.numItems += 1

        load_factor = self.numItems/self.tableSize
        if load_factor > 0.75:  # doubles the hash if load factor greater than 0.75
            self.double()





    def find(self, key):
        """
        Finds the Node in the HashTable with the required key
        :param key: Key that needs to be found
        :return: HashNode with proper key
        """

        loc_index = self.hash_function(key)

        key_exist = self.table[loc_index].find(key)  # finds the key in the index linked list
        if key_exist:
            return key_exist  # return the hash node with the key
        else:
            return False  # key doesn't exist

    def lookup(self, key):
        """
        Finds the value of the required key in the HashTable ADT
        :param key: string corresponding to the value
        :return: Value corresponding to the key
        """

        hash_node = self.find(key)
        if hash_node:
            return hash_node.value  # return the value of the key
        else:
            return False

    def delete(self, key):
        """
        Removed the node from the Hash ADT with the provided key
        :param key: Node that needs to be deleted
        :return: None
        """

        loc_index = self.hash_function(key)
        hash_node = self.find(key)
        self.numItems -= 1
        if hash_node:
            self.table[loc_index].remove(hash_node)  # deletes the Node with the key if it exist in the Hash

    def double(self):
        """
        When the load factor on the hash table is greater than 0.75 this function double the size of the HashTable
        :return: None
        """

        new_hashtable = [LinkedList() for i in range(self.tableSize*2)]  # new list of linked list with 2x size
        for i in range(self.tableSize):
            new_hashtable[i] = self.table[i]

        self.table = new_hashtable
        self.tableSize *= 2
        self.rehash()  # re-add all the values to make use of the addition indices in the new list

    def rehash(self):
        """
        Removes all the elements from the hashTable and re-add them according to HashTable ADT rules
        :return: None
        """

        for i in range(self.tableSize):
            linked_bucket = self.table[i]
            self.table[i] = LinkedList()  # removes all the value from each index
            if linked_bucket.head is not None:
                temp_node = linked_bucket.head
                while temp_node is not None:
                    in_value = temp_node.value
                    in_key = temp_node.key
                    self.insert(in_key, in_value)  # re-add all the values from the removed list
                    self.numItems -= 1
                    temp_node = temp_node.next

def FindWords(phrase, k):
    """
    Finds the sliding window of strings in the  phrase and correspond them to the number of times they appear
    in the string.
    :param phrase: Phrase that needs to be checked for sliding window
    :param k: The number of required times the string should appear in the phrase
    :return: Set of strings that appear k times in the phrase
    """

    word_hash_table = HashTable()  # create hash table
    phrase = phrase.lower()
    for i in range(len(phrase)):  # Sliding window of the string algorithm
        for j in range(i, len(phrase)+1):
            string_to_add = phrase[i:j]
            if len(string_to_add) >= 2:  # only considers string greater than 2 length
                word_exist = word_hash_table.find(string_to_add)  # checks if the string already exists in the Table
                if word_exist:
                    word_exist.value += 1  # Increment the value of the key if string exist
                else:
                    word_hash_table.insert(string_to_add, 1)  # Insert string into the hash if the key doesn't exist

    phrase_set = set()
    for word_linked_list in word_hash_table.table:
        temp_node = word_linked_list.head
        while temp_node:
            if temp_node.value == k:  # looks for all the element in the hash with value equal to k, add them to a set
                phrase_set.add(temp_node.key)
            temp_node = temp_node.next

    return phrase_set
