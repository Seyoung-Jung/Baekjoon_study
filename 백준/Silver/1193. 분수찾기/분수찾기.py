N = int(input())
i, j = 1, 1
up = False
num = 1
for k in range(2, N + 1):
    if num + k >= N:
        if up:
            i = int(k)
            j = 1
            for l in range(num + 2, N + 1):
                i -= 1
                j += 1
        else:
            j = int(k)
            i = 1
            for l in range(num + 2, N + 1):
                j -= 1
                i += 1
        break
    num += k
    up = not up
print(i, '/', j, sep='')