N = [i for i in range(2, 10001)]
Primes = []
while N[0] < (10001 ** 0.5 + 1):
    p = N[0]
    Primes.append(p)
    for n in N:
        if n % p == 0:
            N.remove(n)
Primes.extend(N)

T = int(input())
Goldbach = []
for _ in range(T):
    n = int(input())
    gold_num = n // 2
    while True:
        if gold_num in Primes and (n - gold_num) in Primes:
            Goldbach.append([(n - gold_num), gold_num])
            break
        gold_num += 1

for g in Goldbach:
    print(g[0], g[1])