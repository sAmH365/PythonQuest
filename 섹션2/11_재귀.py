# 반복을 위해 재귀를 사용
# 반복문으로 탐색 하기 힘든 비선형구조에 좋음

# 재귀함수 만드는법
# 1. 종료조건
# 2. 재귀 호출
# 2-1 문제를 더 작은 문제로 쪼개는 재귀 호출

def countdown(n):
  if n == 1:
    return "1 end"

  rec_res = countdown(n - 1)

  text = str(n) + ', ' + rec_res

  return text

print(countdown(4))