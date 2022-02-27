def wordBreak(words, word, out=''):
    if not word:
        print(out.lstrip())

    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in words:
            wordBreak(words, word[i:], out + ' ' + prefix)

lines = []
wordList = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line.strip().split())


for x in range(1, len(lines) - 1):
    wordList.append(lines[x][0])

word = lines[-1][0]

wordBreak(wordList, word)