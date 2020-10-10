index = 999

while index >= 100:
    palindrome = int(index * 1000 + (index % 10) * 100 + (index % 100 - index % 10) + (index - index % 100) / 100)

    for number in range(100, 1000):
        if palindrome / number % 1 == 0:
            if palindrome / number < 1000:
                print(palindrome)

                break
    
    index -= 1