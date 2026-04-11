class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.left = Node()#left.nxt = LRU
        self.right = Node()#Last
        
        self.left.nxt = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
        elif len(self.cache) == self.capacity:
            # print(self.cache.keys())
            # print(key)
            # print(self.left.nxt.key)

            removeNode = self.left.nxt
            self.cache.pop(removeNode.key)
            self.remove(removeNode)
            
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev = self.right.prev

        self.right.prev = node
        node.nxt = self.right
        node.prev = prev

        prev.nxt = node
        # print(node.key)
        # print(self.left.nxt.key)
        # print(self.right.prev.key)
