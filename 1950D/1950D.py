import math
def check_binary(x):
    for digit in str(x):
        if digit not in ["0", "1"]:
            return False
    return True
def is_binary_factor(n):
    if(check_binary(n)):
        return True
    upper = math.ceil(n ** 0.5)
    for j in range(1, upper + 1):
        if(n%j==0)and(check_binary(j)) and (n//j!=n):
            return is_binary_factor(n//j)
    return False

t = int(input())

for i in range(t):
    n = int(input())
    if is_binary_factor(n):
        print("YES")
    else:
        print("NO")