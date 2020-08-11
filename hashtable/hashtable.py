class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)] 
        self.nodeCount = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # load factor = number of items in hash table / total number of slots
        return self.nodeCount / self.storage


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
    
        for c in key:
            hash = ((hash * 33) + ord(c)) % 0x100000000
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #self.storage[self.hash_index(key)] = HashTableEntry(key, value)

        
        bucket_index = self.hash_index(key)

        new_node = HashTableEntry(key, value)
        current_node = self.storage[bucket_index]

        # find the start of the linked list using the index
        # Search through linked list
        if current_node:
            last_node = None
            while current_node:
                # IF the key already exists in the linked list
                    # Replace the value
                if current_node.key == key:
                    # find current key, replace value
                    current_node.value = value
                    return
                last_node = current_node
                current_node = current_node.next
            # if we get this far, we didnt find an current key
            # so we just append the enw node to the end of the storage
            last_node.next = new_node
            # Else
                # Add new HashTable Entry to the head of linked list​
        else:
                self.storage[bucket_index] = new_node


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # if self.storage[self.hash_index(key)] is not None:
        #     self.storage[self.hash_index(key)] = None
        # else: 
        #     return None

        # hash the key and get an index
        bucket_index = self.hash_index(key)

        # Search through the linked list for the matching key
        # Delete that node
        current_node = self.storage[bucket_index]
        if current_node:
            last_node = None
            while current_node:
                if current_node.key == key:
                    if last_node:
                        last_node.next = current_node.next
                    else:
                        self.storage[bucket_index] = current_node.next
                # Return value of deleted node (or None)
                last_node = current_node
                current_node = current_node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # if self.storage[self.hash_index(key)] is not None:
        #     return self.storage[self.hash_index(key)].value
        # else:
        #     return None

        # hash the key and get an index
        bucket_index = self.hash_index(key)

        # Get the linked list AT the computed index
        # Search through the linked list for the key
        #   Compare keys until you find the right one
        current_node = self.storage[bucket_index]
        # If it exists, return the value
        if current_node:
            while current_node:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
        # else, return None
        return None
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Make a new array thats DOUBLE the current size
        newArr = [None] * new_capacity
        oldArr = self.storage
        self.storage = newArr
        self.capacity = len(newArr)

         # Go through each linked list in the array
        for node in oldArr:
            # GO through each item and re-hash it
            if node is not None:
                current_node = node
                # Insert the items into their new locations
                while current_node is not None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
