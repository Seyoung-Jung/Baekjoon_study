N = int(input())
X = list(map(int, input().split()))
prime = 0
for x in X:
    if x == 1:
        is_prime = False
        continue
    else:
        is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        prime += 1
print(prime)