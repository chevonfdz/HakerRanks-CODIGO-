lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line.strip().split())

R = int(lines[0][0])
C = int(lines[0][1])


def issafe(i, j):
    if 0 <= i < R and 0 <= j < C:
        return True
    return False


def rotLemons(v):
    changed = False
    no = 2
    while True:
        for i in range(R):
            for j in range(C):
                if v[i][j] == no:
                    if (issafe(i + 1, j) and
                            v[i + 1][j] == 1):
                        v[i + 1][j] = v[i][j] + 1
                        changed = True

                    if (issafe(i, j + 1) and
                            v[i][j + 1] == 1):
                        v[i][j + 1] = v[i][j] + 1
                        changed = True

                    if (issafe(i - 1, j) and
                            v[i - 1][j] == 1):
                        v[i - 1][j] = v[i][j] + 1
                        changed = True

                    if (issafe(i, j - 1) and
                            v[i][j - 1] == 1):
                        v[i][j - 1] = v[i][j] + 1
                        changed = True

        if (not changed):
            break
        changed = False
        no += 1

    for i in range(R):
        for j in range(C):
            if v[i][j] == 1:
                return -1
    return no - 2


if __name__ == "__main__":

    for i in lines:
        for j in range(0, len(i)):
            i[j] = int(i[j])

    v = []

    for x in range(1, len(lines)):
        v.append(lines[x])

    print(rotLemons(v))
