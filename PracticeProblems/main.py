def selectNum(num):
    if num <= 1 or num >= 100:
        return num
    if num % 2 == 1:
        print("Weird")
    elif num % 2 == 0 and 2 <= num <= 5:
        print("Not Weird")
    elif num % 2 == 0 and 6 <= num <= 20:
        print("Weird")
    elif num % 2 == 0 and num > 20:
        print("Not Weird")

if __name__ == '__main__':
    num = int(input().strip())
    selectNum(num)

