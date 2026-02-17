# 배열 생성

# 0으로 초기화된 배열 생성 (길이 10)
arr = [0 for _ in range(10)]
print(arr)

# 정해진 개수만큼 입력받기
arr2 = [ _ + 1 for _ in range(3)]
print(arr2)

# 다른 배열 참고하여 배열 생성
arr3 = [ 2 * ele for ele in arr2]
print(arr3)

# 배열 추출하기
## 배열에서 3의 배수인 원소만 추출해 새로운 배열 만들기
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_arr = [ele for ele in arr if ele % 3 == 0]
print(new_arr)
## 짝수만 찾기
new_arr2 = [ele for ele in arr if ele % 2 == 0]
print(new_arr2)

# 삼항연산자
a = 10
b = '참' if a > 3 else '거짓'
print(b)

# 배열에서 짝수는 음수로, 홀수는 그대로 담은 새로운 배열 만들기
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_arr = [-ele if ele % 2 == 0 else ele for ele in arr]
print(new_arr)
new_arr = [-ele if ele % 2 == 0 else ele for ele in new_arr]
print(new_arr)

# 두 배열 참고해서 새로운 배열 만들기
arr1 = [100, 200, 300, 400]
arr2 = [1, 2, 3]

# arr3 = [arr1[i] + arr2[i] for i in range(len(arr1))]
# print(arr3)

arr4 = [el1 + el2 for el1 in arr2 for el2 in arr1]
print(arr4)

arr4 = []
for idx1, value1 in enumerate(arr2):
  for idx2, value2 in enumerate(arr1):
    arr4.append(value1 + value2)
print(arr4)

# ====== gugu class =====
# times_table = int(input('몇 단을 출력할까요?'))
# num = int(input('몇 까지 곱해 볼까요?'))
# for i in range(num):
#   print(f'{times_table} x {i + 1} = {times_table * (i + 1)}')
#  2 * 1, 3 * 1, 4 * 1
# num = int(input('몇 단까지 출력 할 까요?'))
num = 4
for idx1 in range(1, 10):
  for idx2 in range(2, num + 1):
    print(f'{idx2} x {idx1} = {idx2 * idx1:2d}', end='\t')
  print()

print('\n 2차원 배열 생성 =======================')
# 2차원 배열 생성
# 0 으로 초기화된 N * M 2차원 배열 만들기(N 행 M열)
N, M = 3, 5
arr_2D = []

for i in range(N):
  row = []
  for j in range(M):
    row.append(0)
  arr_2D.append(row)
print(arr_2D)

print()
print('2차원 배열 쉽게 출력하는 법  *배열, sep="\\n"')
# 2차원 배열 쉽게 출력하는 법
# *배열
print(*arr_2D, sep='\n')

print('\n 2차원 배열 생성 (리스트컴프리헨션) =======================')
N, M = 3, 5

