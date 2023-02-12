N = int(input())
answer = int(N)
for i in range(N):
    S = input()
    group = []
    for s in S:
        if group and s in group[:-1]:
            answer -= 1
            break
        elif group and s == group[-1]:
            continue
        else:
            group.append(s)
print(answer)