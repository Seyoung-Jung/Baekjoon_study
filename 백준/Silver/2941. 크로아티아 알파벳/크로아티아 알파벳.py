Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
alphabet_num = 0
for c in Croatia:
    if c in S:
        alphabet_num += S.count(c)
        S = S.replace(c, ' ')
S = S.replace(' ', '')
alphabet_num += len(S)
print(alphabet_num)