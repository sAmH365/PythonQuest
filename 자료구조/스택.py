class ArrayStack:
  def __init__(self, capacity):
    self.stack = [None] * capacity
    self.capacity = capacity
    self.top = -1

  def push(self, item):
    if self.top + 1 == self.capacity:
      raise Exception("Stack is full")
    self.top += 1
    self.stack[self.top] = item

  def pop(self):
    if self.is_empty():
      raise Exception("Stack is Empty")
    item = self.stack[self.top]
    self.top -= 1
    return item

  def peek(self):
    if self.is_empty():
      raise Exception("Stack is Empty")

    return self.stack[self.top]

  def is_empty(self):
    return self.top == -1

  def size(self):
    return self.top + 1


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedListStack:
  def __init__(self):
    self.head = None
    self.count = 0

  def push(self, item):
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node
    self.count += 1

  def pop(self):
    if self.is_empty():
      raise Exception("Stack is Empty")

    item = self.head.data
    self.head = self.head.next
    self.count -= 1

    return item

  def peek(self):
    if self.is_empty():
      raise Exception("Stack is Empty")
    return self.head.data

  def is_empty(self):
    return self.count == 0

  def size(self):
    return self.count
