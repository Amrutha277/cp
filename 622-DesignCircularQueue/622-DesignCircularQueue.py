# Last updated: 9/25/2025, 9:56:43 AM
class MyCircularQueue:

    def __init__(self, k: int):
        self.k= k
        self.q = [0]*k
        self.head= self.tail = 0
        self.size= 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.q[self.tail] = value
        self.tail = (self.tail+1)%self.k
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.size ==0:
            return False
        
        self.head = (self.head+1)%self.k
        self.size -=1
        return True
        
    def Front(self) -> int:
        if self.size ==0:
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.size ==0:
            return -1
        
        last_index = (self.tail -1 + self.k) %self.k
        return self.q[last_index]

    def isEmpty(self) -> bool:
        return self.size ==0

    def isFull(self) -> bool:
        return self.size ==  self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()