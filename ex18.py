import math

numbers = [2, 3, 2, 3, 2, 0, 0, 5, 7, 7, 6, 6, 3, 5, 5, 4]
product = []
total = 0

for i,e in enumerate(numbers):
    if (i % 2) == 0:
        if (e * 2) > 9:
            product.append((e * 2) - 9)
        else:
            product.append(e * 2)
    else:
        product.append(e * 1)

for each in product:
    total += each


lastDigit = total % 10
if lastDigit == 0:
    print("The number is valid according to the Luhn formula. Total : " + str(total))
else:
    print("The number is not valid according to the Luhn formula. Total : " + str(total))
    if len(product) < 16:
        print("Incomplete version : " + str(product))
        digits = int(math.log10(total))
        firstDigit = int(total / pow(10, digits))
        totalPlanned = (firstDigit + 1) * 10
        missingDigit = totalPlanned - total
        product.append(missingDigit)
        print("Complete version : " + str(product))
        print("Now the number is valid according to the Luhn formula ('" + str(missingDigit) + "' was missing). Total : " + str(totalPlanned))
