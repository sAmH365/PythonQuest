import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

input_arr = [v for v in range(1, N + 1)]


def solve(index: int, current_arr: list):
  if len(current_arr) == M:
    print(*current_arr)
    return

  for i in range(index, len(input_arr)):
    current_arr.append(input_arr[i])
    solve(i + 1, current_arr)
    current_arr.pop()

solve(0, [])