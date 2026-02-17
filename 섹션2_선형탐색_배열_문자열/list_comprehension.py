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
arr1 = [100, 200, 300]
arr2 = [1, 2, 3]

arr3 = [i for i in range(len(arr1))]
print(arr3)