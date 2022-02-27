def calculateSum(n):
    total = 0
    newTotal = 0
    fTotal = 0
    number = list(map(int, str(n)))
    for i in range(0, len(number)):
        total = total + number[i]

    number2 = list(map(int, str(total)))
    for x in range(0, len(number2)):
        newTotal = newTotal + number2[x]

    number3 = list(map(int, str(newTotal)))
    for y in range(0, len(number3)):
        fTotal = fTotal + number3[y]
    return fTotal


print(calculateSum(int(input("Enter a number: "))))