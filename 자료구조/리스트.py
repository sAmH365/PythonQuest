class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head: Node = None

  def insert_at_head(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_position(self, data, position = 0):
    if position == 0:
      self.insert_at_head(data)
      return

    current = self.head
    for _ in range(position - 1):
      if current is None:
        return
      current = current.next

    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node

  def delete_at_position(self, position):
    if self.head is None:
      return

    current = self.head
    if position == 0:
      self.head = current.next
      return

   # 0, 1, 2, 3  -> 0, 2, 3

    for _ in range(position - 1):
      if current.next is None:
        return
      current = current.next

    if current.next is None:
      return
    current.next = current.next.next
    return

sl = SinglyLinkedList()

sl.insert_at_position(0, 0)
sl.insert_at_position(1, 1)
sl.insert_at_position(2, 2)
sl.insert_at_position(3, 3)
sl.insert_at_position(4, 4)

sl.delete_at_position(5)


print(sl.head.data)
print(sl.head.next.data)


