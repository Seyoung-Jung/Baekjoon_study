Dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
answer = len(S) * 2
for s in S:
    answer += [Dial.index(d) + 1 for d in Dial if s in d][0]
print(answer)