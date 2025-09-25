# Last updated: 9/25/2025, 9:24:13 AM
class LRUCache:
    """
    LRU Cache = Hash Map (key -> node)  +  Doubly Linked List (MRU at head).
    All public ops run in O(1) average time.
    """

    # ------------ doubly linked list node ------------
    class _Node:
        __slots__ = ("key", "val", "prev", "next")   # keeps every node lightweight (no __dict__)
        def __init__(self, key: int, val: int):
            self.key, self.val = key, val
            self.prev = self.next = None             # neighbours in the DLL

    # ------------ ctor ------------
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}                                # key -> _Node
        # create two sentinel nodes and link them: head <-> tail
        self.head, self.tail = self._Node(0, 0), self._Node(0, 0)   # tuple unpacking
        self.head.next, self.tail.prev = self.tail, self.head

    # ------------ internal DLL helpers ------------
    def _add_to_front(self, node):
        """Insert `node` right after head (mark as MRU)."""
        node.prev, node.next = self.head, self.head.next  # pointer surgery
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Detach `node` from its current position."""
        prev_, nxt_ = node.prev, node.next
        prev_.next, nxt_.prev = nxt_, prev_

    def _move_to_front(self, node):
        """Make an existing node MRU."""
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self):
        """Remove & return the least-recently-used node (one before tail)."""
        lru = self.tail.prev
        self._remove(lru)
        return lru

    # ------------ public API ------------
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)                     # mark as MRU
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:                           # update path
            node = self.map[key]
            node.val = value
            self._move_to_front(node)
        else:                                         # insert path
            node = self._Node(key, value)
            self.map[key] = node
            self._add_to_front(node)
            if len(self.map) > self.cap:              # eviction needed
                lru = self._pop_lru()
                del self.map[lru.key]
