import random

test_arr = random.sample(range(1, 51), 20)

print(test_arr)

def insertion_sort(arr):

  for i in range(1, len(arr)):
    target = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > target:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = target

  return arr


print(insertion_sort(test_arr))