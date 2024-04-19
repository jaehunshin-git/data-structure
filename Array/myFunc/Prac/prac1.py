a = []
for i in range(0, 4):
    a.append(int(input()))

print(a)

sum = 0

for i in a:
    sum += i

result = sum / len(a)

print(result)