import random

test_arr = random.sample(range(1, 51), 20)

print(test_arr)

# def insertion_sort(arr):
#
#   for i in range(1, len(arr)):
#     target = arr[i]
#     j = i - 1
#
#     while j >= 0 and arr[j] > target:
#       arr[j + 1] = arr[j]
#       j -= 1
#
#     arr[j + 1] = target
#
#   return arr
#
#
# print(insertion_sort(test_arr))


def merge_sort(arr, left, right) -> list:
  if left >= right:
    return arr

  mid = (left + right) // 2
  merge_sort(arr, left, mid)
  merge_sort(arr, mid + 1, right)
  merge(arr, left, mid, right)

  return arr

def merge(arr, left, mid, right):
  tmp = []
  i = left
  j= mid + 1

  while i <= mid and j <= right:
    if arr[i] <= arr[j]:
      tmp.append(arr[i])
      i += 1
    else:
      tmp.append(arr[j])
      j += 1

  while i <= mid:
    tmp.append(arr[i])
    i += 1
  while j <= right:
    tmp.append(arr[j])
    j += 1

  for t in range(len(tmp)):
    arr[left + t] = tmp[t]

  return arr
print(*merge_sort(test_arr, 0, len(test_arr) - 1))