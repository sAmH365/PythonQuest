# 시간초과
import sys

input = sys.stdin.readline

N, L = list(map(int, input().split()))

def check_arr_length(arr):
  return L <= len(arr) < 100

result = set()
def find_num_arr():
  for i in range(N + 1):
    sum = i
    num_arr = [i]
    for j in range(i + 1, N + 1):
      if sum == N:
        result.add(tuple(num_arr))
      elif sum > N:
        break
      else:
        sum += j
        num_arr.append(j)

find_num_arr()


sorted_list = sorted(result, reverse=True)
target_arr = [v for v in sorted_list if L <= len(v) < 100]


print(target_arr)

if len(target_arr) == 0:
  print(-1)
else:
  print(*target_arr[0])