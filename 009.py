for a in range(1, 1001):
    for b in range(a, 1001):
        if (a ** 2 + b ** 2) ** (1/2) % 1 == 0:
            if a + b + (a ** 2 + b ** 2) ** (1/2) == 1000:
                print(a * b * (a ** 2 + b ** 2) ** (1/2))