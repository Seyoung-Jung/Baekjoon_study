def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

N = 123456
all_num = [i for i in range(2, 2 * N + 1)]
prime = []
for a in all_num:
    if is_prime(a):
        prime.append(a)

Bertrand = []
while True:
    n = int(input())
    if n == 0:
        break
    Bertrand.append(sum([i > n and i <= 2*n for i in prime]))
for b in Bertrand:
    print(b)