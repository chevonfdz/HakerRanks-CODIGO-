lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line.strip().split())

for i in lines:
    for j in range(0, len(i)):
        i[j] = int(i[j])

count = lines[0][0]

for x in range(1, count+1):
    f = lines[x][0]
    t = lines[x][1]
    b = lines[x][2]

    m = t%f
    if m == 0:
        print(f)
    else:
        print(m+(b-1))
