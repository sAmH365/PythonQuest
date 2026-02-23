from itertools import permutations

my_arr = list(range(1, 5))
result = list(permutations(my_arr, 4))
print(len(result))
print(result)

# 1 2 3 4

def manual_permutations(arr, r):
  results = []

  def backtrack(current_path, remaining_elements):
    # 1. 종료 조건: 선택된 개수가 r개와 같을 때
    if len(current_path) == r:
      results.append(tuple(current_path))
      return

    # 2. 남은 요소들을 하나씩 순회하며 선택
    for i in range(len(remaining_elements)):
      next_element = remaining_elements[i]
      # 현재 요소를 제외한 나머지 리스트 생성
      new_remaining = remaining_elements[:i] + remaining_elements[i + 1:]

      # 다음 단계로 이동
      backtrack(current_path + [next_element], new_remaining)

  backtrack([], arr)
  return results


# 사용 예시
my_arr = [1, 2, 3, 4]
result = manual_permutations(my_arr, 4)
print(result)


def manual_permutations(arr, r):
  results = []
  visited = [False] * len(arr)  # 방문 체크 배열 생성

  def backtrack(current_path):
    if len(current_path) == r:
      results.append(tuple(current_path))
      return

    for i in range(len(arr)):
      if not visited[i]:  # 방문하지 않았다면
        visited[i] = True  # [선택]
        backtrack(current_path + [arr[i]])
        visited[i] = False  # [복구] 다음 경우의 수를 위해 해제!

  backtrack([])
  return results

print(manual_permutations(my_arr, 4))
