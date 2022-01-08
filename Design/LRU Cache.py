"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    - to achive accessing in constant time, we use a dictionary. to achieve constant time removal, we use
        a linked List.
    1. we define a doubly linked list node.
    2. we init a LRUCache with the given capacity. we create an empty dict that will act as the cache.
        - we define left and right, and init them to empty nodes.
        - left pointer's next will point to our LRU node.
        - right pointer's prev will point to the most commonly used element.
    3. let left's next point to right and right's prev point to left.
    4.  create remove and insert helper methods.
    5. complete get and put methods.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        #left is the LRU and right is most recent
        self.left.next = self.right
        self.right.prev = self.left

    #code to purge a node
    def remove(self, node):
        """
        - given the node you want to remove, get its prev and next. assign its prev.next to next
        and assign its next.prev to prev
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #code to insert a node to the right
    def insert(self, node):
        """
        - get the last node: self.right.prev
        - assign last node next to the new node
        - make the right pointer prev point to the new node
        """
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev
        prev.next = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        """
        - check if the key exists in our cache. if it exists:
            - remove and add it again in the right side(most commonly use)
        - else, return -1
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        put update val if it exists, else add a new node
        - if the key exists, remove it.
        - create a new node with the given value and insert it.
        - if the new length of the cache exceeds our capacity, get the
            LRU and remove it from the cache and the linked list.

        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]