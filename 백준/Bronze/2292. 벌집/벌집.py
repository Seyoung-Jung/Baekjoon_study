n = int(input())

nums_pileup = 1
answer = 1
while n > nums_pileup :
    nums_pileup += 6 * answer
    answer += 1
print(answer)