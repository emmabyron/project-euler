answer = []
number = 600851475143

index = 2

while index <= 600851475143 ** (1/2):
    if number % index == 0:
        answer.append(index)

        number /= index
    else:
        index += 1

print(answer)