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


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedListQueue:
  def __init__(self):
    self.front = None
    self.rear = None

  # 3   1 2

  def enqueue(self, item):
    new_node = Node(item)
    if self.rear is None:
      self.front = self.rear = new_node
      return

    self.rear.next = new_node
    self.rear = new_node

  def dequeue(self):
    if self.is_empty():
      print("queue is empty")
      return None
    item = self.front.data
    self.front = self.front.next
    if self.front is None:
      self.rear = None
    return item

  def display(self):
    current = self.front
    result = []
    while current:
      result.append(current.data)
      current = current.next
    print(result)

  def is_empty(self):
    return self.front is None

lq = LinkedListQueue()

lq.enqueue(1)
lq.enqueue(3)
lq.enqueue(5)
lq.enqueue(2)
lq.enqueue(7)

lq.dequeue()

lq.display()
