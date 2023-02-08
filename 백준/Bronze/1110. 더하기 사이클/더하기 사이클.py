original = int(input())
num = 0
temp = int(original)
while True:
    new = (temp % 10) * 10 + (int(temp / 10) + (temp % 10)) % 10
    num += 1
    temp = int(new)
    if new == original:
        break
print(num)