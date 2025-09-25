# Last updated: 9/25/2025, 9:41:29 AM
class LRUCache:
    
    class _Node:
        __slots__ = ("key", "val", "prev", "next")
        def __init__(self, key:int, val:int):
            self.key, self.val= key, val
            self.prev = self.next= None
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map ={}
        #dummy head and tail and linking them head <-> tail
        self.head, self.tail =  self._Node(0,0), self._Node(0,0)
        self.head.next , self.tail.prev = self.tail, self.head

    def _add_to_front(self,node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next= node
    
    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev= node.prev
    
    def _touch(self, node):
        self._remove(node)
        self._add_to_front(node)
    
    def _pop(self):
        lru= self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node= self.map[key]
        self._touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._touch(node)
            return
        node= self._Node(key, value)
        self.map[key]= node
        self._add_to_front(node)

        if len(self.map)>self.cap:
            old = self._pop()
            del self.map[old.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)