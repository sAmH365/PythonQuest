# 1차원 / 2차원 배열 입력받기 / 가공하기

print('\n 1차원배열 입력받기===================')

# 1차원 배열 입력받기
# arr = list(map(int, input().split()))
# print(arr)

# 인풋 느릴때
import sys
# inputs = sys.stdin.readline()
# arr = list(map(int, inputs.split()))

print('\n 2차원배열 입력받기===================')
# N, M = list(map(int, input().split())) # N행, M열
inputs = sys.stdin.readline

# N, M = list(map(int, inputs().split()))
# arr = [ list(map(int, inputs().split())) for _ in range(N)]
# print(*arr, sep='\n')

# 연습문제1
# 학생 정보를 2차원 리스트로 저장하기
# 점수를 정수형으로 형변환하기
# 틀정 열을 기준으로 정렬하기

my_input = """\
가희 38 D
나희 77 B
다희 51 C
라희 91 A\
"""
my_input = my_input.split('\n')
arr_2D = [ list(el.split(' ')) for el in my_input]

for i in range(4):
  arr_2D[i][1] = int(arr_2D[i][1])

print(*arr_2D, sep = '\n')

# 이름 기준으로 정렬
print(sorted(arr_2D))
# 점수를 기준으로 내림차순 정렬
print(sorted(arr_2D, key = lambda x: x[1], reverse=True))
# 학점을 기준으로 정렬
print(sorted(arr_2D, key = lambda x: x[2]))

# 마무리 연습문제
# 다음과 같이 N이 주어지고, 한 쌍의 숫자가 N번 주어진다 각 숫자 쌍의 합을 순서대로 출력
# 입력예시
# 5
# 1 1
# 12 34
# 5 500
# 40 60
# 1000 1000
import sys
inputs = sys.stdin.readline

N = int(inputs())
arr_2D = [ list(map(int, inputs().split())) for _ in range(N)]

for el in arr_2D:
  print(sum(el))
