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

n = lines[0][0]
ar = lines[1]

all_elems = set(ar)
my_result = 0
for elements in all_elems:
   my_result += ar.count(elements) // 2


print(my_result)