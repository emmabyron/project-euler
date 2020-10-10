answer = sum(number for number in range(101)) ** 2 - sum(number ** 2 for number in range(101))

print(answer)