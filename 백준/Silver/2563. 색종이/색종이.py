XY = [[False] * 100 for _ in range(100)]
area = 0
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if not XY[i][j]:
                XY[i][j] = True
                area += 1
print(area)