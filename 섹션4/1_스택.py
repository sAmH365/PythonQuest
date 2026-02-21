# 스택의 구현: stack = []
# 큐의 구현: queue = deque([]) # from collections import deque

from collections import deque

queue = deque(['user1', 'user2', 'user3'])
print(list(queue))

# popleft() -> 앞쪽에서 꺼냄
# pop() -> 뒤쪽에서 꺼냄
print(queue.popleft(),' :: ' ,list(queue))

# appendleft() -> 앞쪽에 추가
# append() -> 뒤쪽에 추가
queue.append('user4')
print(list(queue))
