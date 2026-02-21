def bs_for(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

num_arr = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]
target_number = 62

print(bs_for(num_arr, target_number))

print('\nbisect===================')
from bisect import *

numbers = [1, 2, 3, 5, 6, 8, 11]
query = 1
left = bisect_left(numbers, query)
right = bisect_right(numbers, query)
print(left, ': Left')
print(right, ': Right')

def bs_bisect(arr, target):
  i = bisect_left(arr, x)

  if i < len(arr) and arr[i] == target:
    return i
  else:
    return -1