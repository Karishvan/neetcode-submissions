class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.mru_ptr = ListNode(0, 0, None, None)
        self.lru_ptr = ListNode(0, 0, self.mru_ptr, None)
        self.mru_ptr.prev = self.lru_ptr

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node == -1:
            return -1
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
        else:
            node = ListNode(key, value, None, None)
            
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            key_to_del = self.lru_ptr.nxt.key
            self.remove(self.lru_ptr.nxt)
            del self.cache[key_to_del]
    #PTR MANIPULATION
    def insert(self, node):
        previous = self.mru_ptr.prev
        previous.nxt = node
        node.prev = previous
        self.mru_ptr.prev = node
        node.nxt = self.mru_ptr

    
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        nxt.prev = prev
        prev.nxt = nxt
        
        
        
class ListNode:
    def __init__(self, key, val, nxt, prev):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev