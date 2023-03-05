N = int(input())
Sort = []
for _ in range(N):
    x = int(input())
    if not Sort:
        Sort.append(x)
    else:
        for i in range(len(Sort)):
            if x < Sort[i]:
                Sort.insert(i, x)
                break
            elif x > Sort[-1]:
                Sort.append(x)
for s in Sort:
    print(s)