S = input().upper()
counts = {}
for s in set(S):
    counts[s] = S.count(s)
max_key = [k for k, v in counts.items() if v == max(counts.values())]
if len(max_key) > 1:
    print('?')
else:
    print(max_key[0])