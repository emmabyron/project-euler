primes = [2]

index = 3

while True:
    if len(primes) >= 10001:
        break

    for p in primes:
        if p > index ** (1/2):
            primes.append(index)

            break

        if index / p % 1 == 0:
            break
    
    index += 2

print(primes[10000])