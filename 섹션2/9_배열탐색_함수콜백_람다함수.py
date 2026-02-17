# 가장 기초적인 for문을 이용한 탐색

# 배열 내 최대값 찾기
arr = [1, 2, 4, 6, 1, 2, 3]
max_value = float('-inf')
for n in arr:
  if n > max_value:
    max_value = n
print(max_value)
print()


print('\n콜백함수===================')
# 콜백
# 다른 함수를 인자로 받는 함수 선언
def caller(func, n):
  return func(n)

# 콜백 함수로 사용될 함수 2개 선언
def square(n):
  return n * n

def minus_one(n):
  return n -1
print(caller(square, 10))
print(caller(minus_one, 10))

print('\n내장함수===================')

# 배열의 모든 원소를 정수로 바꾸자
arr = ['1', '3', '7', '19', '33']
print(type(arr[1]))

res = list(map(int, arr))
print(type(res[1]))
print(res)

# 배열의 원소가 100이 넘으면 -1, 안 넘으면 그대로 두자
arr = [1, 201, 44, 33, 2, 105]

def over_hundred(n):
  if n > 100:
    return -1
  else:
    return n

res = list(map(over_hundred, arr))
print(res)

print('\n정렬 :: sorted===================')
set_numbers = (8, 3, 9, 1, 5)

# 기본 오름차순
unique_numbers = sorted(set_numbers)
print(unique_numbers)
# 내림차순 정렬
unique_numbers = sorted(set_numbers, reverse = True)
print(unique_numbers)

print('\n zip 내장함수===================')
# 이름, 점수 리스트를 받아 zip & 리스트로 변환 후, 점수 내림차순으로 sort
l1 = ['Amy', 'Cam', 'Bob']
l2 = [81, 62, 79]

zipped = list(zip(l1, l2))
print(zipped)
print(sorted(zipped))

# 튜플의 두 번째 원소를 기준으로 sort하려면
def cb_f(tup):
  return tup[1]
#sorted함수의 인자로 Key = function name 넣기
print(sorted(zipped, key = cb_f))
print(sorted(zipped, key = cb_f, reverse = True))

# 람다함수 사용
sorted_by_num = sorted(zipped, key = lambda x: x[1])
print(f'sorted_by_score = {sorted_by_num}')
print()

# map() 함수의 인자(콜백함수)로 람다함수 쓰기
# 리스트 입력받아 각 리스트의 원소 제곱한 리스트 반환하기
input_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(map(lambda x: square(x), input_l))
print(res)

# 이름, 점수 리스트 받아 zip & 리스트로 변환 후, 점수 내림차순으로 sort
l1 = ['Amy', 'Cam', 'Bob']
l2 = [81, 62, 79]
zipped = list(zip(l2, l1))
res = list(sorted(zipped, key = lambda x: x[1], reverse = True))
print(res)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print(list(zip(names, scores, strict=True)))