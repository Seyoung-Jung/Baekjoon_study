S = input().upper()
counts = {}
for s in set(S):
    counts[s] = S.count(s)
if list(counts.values()).count(max(counts.values())) > 1:
    print('?')
else:
    print([k for k, v in counts.items() if v == max(counts.values())][0])
