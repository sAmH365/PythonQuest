def permutation(n, r):
  result = 1
  for i in range(n, n - r, -1):
    result *= i
  return result

def facto(n):
  if n <= 0:
    return 1

  result = 1
  for i in range(n, 0, -1):
    result *= i
  return result

def combination(n, r):
  return int(permutation(n, r) / facto(r))

print(permutation(10, 8))
print(permutation(7, 2))

print(combination(8, 4))