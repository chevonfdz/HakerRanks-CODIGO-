def prod(k):
    pr = 1
    for d in str(k):
        pr *= int(d)
    return pr

rez = []
for _ in range(int(input())):
    mn, mx = map(int, input().split())
    rez.append(max(range(mn, mx + 1), key=prod))
print(*rez, sep='\n')

ans = int(input())
print(prod(ans))