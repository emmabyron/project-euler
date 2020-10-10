answer = [0, 0]

for number in range(1, 1000001):
    length = 0
    current = number

    while current > 1:
        if current % 2 == 0:
            current /= 2
            length += 1
        else:
            current *= 3
            current += 1
            length += 1
    
    if length > answer[0]:
        answer = [length, number]

print(answer[1])