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

print('\n피보나치====================')
my_fibo_dict = {}
def fibo(n):
  if n <= 0:
    return None

  if n == 1 or n == 2:
    return 1

  if n in my_fibo_dict:
    return my_fibo_dict[n]

  cur_n = fibo(n - 1) + fibo(n - 2)

  my_fibo_dict[n] = cur_n

  return cur_n

print(fibo(100))

print('\n진법 변환 ====================')
def trans(target, formation):
  chars = "0123456789ABCDEF"

  share = target // formation
  remain = target % formation

  if share == 0:
    return chars[remain]

  cur_trans = trans(share, formation)

  return str(cur_trans) + str(chars[remain])

print(trans(258, 2))

print('\n회문구조 판별 ====================')
def palindrome(text, idx=0):
  text = text.upper()
  if idx == len(text) // 2:
    return True

  print(idx, text[idx], text[-(idx + 1)])

  if text[idx] == text[-(idx + 1)]:
    return palindrome(text, idx + 1)
  else:
    return False

test = 'ab101ba'
print(len(test))
print(palindrome(test))

def is_palindrome(s):
  if len(s) <= 1:
    return True

  print(s, s[1:-1])

  if s[0] != s[-1]:
    return False
  else:
    return is_palindrome(s[1:-1])

res = is_palindrome('ab101ba')
print(res)

print('\n중첩된 리스트 풀기 ====================')
#중첩된 리스트 주어짐 -> 내부괄호 모두 풀어 중첩 없는 리스트 반환
# input: [1, [2,3,4], [5,6,[7,8]]]
# output: [1, 2, 3, 4, 5, 6, 7, 8]

def unpack_list(nested_list, unpacks = []):
  for el in nested_list:
    if type(el) == list:
      unpack_list(el, unpacks)
    else:
      unpacks.append(el)

  return unpacks

inputs = [1, [2,3,4], [5,6,[7,8]]]
# inputs = [1, [2, 3]]
print(unpack_list(inputs))

def flatten(l):
  if not isinstance(l, list):
    return [l]

  res = []
  for item in l:
    res += flatten(item)
  return res


def mult_two(n):
  j = 1
  while j * 2 <= n:
    print(j)
    j *= 2
  return j

print(mult_two(18))