N = int(input())
if N < 100:
    hansu = int(N)
else:
    hansu = 99
    for i in range(111, N + 1):
        a = i // 100
        b = (i // 10) % 10
        c = i % 10
        if b - a == c - b:
            hansu += 1
print(hansu)