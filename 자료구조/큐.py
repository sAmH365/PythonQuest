class ArrayQueue:
  def __init__(self, capacity):
    self.queue = [None] * capacity
    self.capacity = capacity
    self.front = 0
    self.rear = 0
    self.size = 0

  def enqueue(self, item):
    if self.is_full():
      raise Exception('queue is full')
    self.queue[self.rear] = item
    self.rear = (self.rear + 1) % self.capacity
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      raise Exception('queue is empty')
    item = self.queue[self.front]
    self.front = (self.front + 1) % self.capacity
    self.size -= 1
    return item

  def peek(self):
    if self.is_empty():
      raise Exception('queue is empty')
    return self.queue[self.front]

  def traverse(self):
    for i in range(self.size):
      index = (self.front + i) % self.capacity
      print(self.queue[index])

  def is_empty(self):
    return self.size == 0

  def is_full(self):
    return self.size == self.capacity


aq = ArrayQueue(10)

aq.enqueue(1)
aq.enqueue(3)
aq.enqueue(5)
aq.enqueue(2)
aq.enqueue(7)

aq.traverse()