def d(n):
    ans = int(n)
    while n > 9:
        ans += n % 10
        n //= 10
    ans += n
    return ans

for i in range(1, 10000):
    self_number = True
    for j in range(i, 0, -1):
        if d(j) == i:
            self_number = False
            break
    if self_number:
        print(i)