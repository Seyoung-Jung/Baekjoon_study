T = int(input())
answer = []
for i in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n + 1)]
    if k > 0:
        for j in range(k):
            tmp = []
            for l in range(n):
                tmp.append(sum(people[:(l+1)]))
            people = tmp
    answer.append(people[-1])
for a in answer:
    print(a)