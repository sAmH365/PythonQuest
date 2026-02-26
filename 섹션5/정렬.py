import random

print('=================버블정렬==================')
test_arr = random.sample(range(1, 10), 4)
print(test_arr)

def bubble_sort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr

print(*bubble_sort(test_arr))



print('\n=================삽입정렬==================')
test_arr1 = random.sample(range(1, 51), 20)
print(test_arr1)
def insertion_sort(arr):

  for i in range(1, len(arr)):
    target = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > target:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = target

  return arr


print(insertion_sort(test_arr1))

print('\n=================병합정렬==================')
test_arr2 = random.sample(range(1, 51), 20)
print(test_arr2)
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
print(*merge_sort(test_arr2, 0, len(test_arr2) - 1))

print('\n=================퀵정렬==================')
test_arr3 = random.sample(range(1, 51), 20)
print(test_arr3)

def quick_sort(arr, left, right):
  if left < right:
    pi = partition(arr, left, right)
    quick_sort(arr, left, pi - 1)
    quick_sort(arr, pi + 1, right)

  return arr

def partition(arr, left, right):
  pivot = arr[right]
  i = left - 1
  for j in range(left, right):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[right] = arr[right], arr[i + 1]

  return i + 1

print(*quick_sort(test_arr3, 0, len(test_arr3) - 1))