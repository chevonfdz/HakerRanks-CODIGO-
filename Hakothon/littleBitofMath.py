def cf(num1,num2):
    n=[]
    for i in range(1, min(num1, num2)+1):
        if num1%i==num2%i==0:
            n.append(i)
    return n

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line.strip().split())

a = int(lines[0][0])
b = int(lines[0][1])

print(len(cf(a,b)))