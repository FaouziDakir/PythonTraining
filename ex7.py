n = 10
squareOfSum = 0
sumOfSquares = 0

for i in range(1, n + 1):
    squareOfSum += i
    sumOfSquares += i ** 2

squareOfSum = squareOfSum ** 2

print('the difference between the square of the sum of the first ' + str(n) + ' natural numbers and the sum of the squares is ' + str(squareOfSum - sumOfSquares))
