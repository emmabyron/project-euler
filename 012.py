triangle = 0
index = 0

divisors = 0

while divisors < 500:
    index += 1
    triangle += index
    divisors = 0

    for number in range(1, int(triangle ** (1/2) // 1)):
        if triangle / number % 1 == 0:
            divisors += 2

print(triangle)