def UsernameValidation(strParam):
    x = "false"
    y = "true"
    if len(strParam) < 4 or len(strParam) > 25:
        return x

    if not str(strParam[0]).isalpha():
        return x

    if str(strParam[-1]) == '_':
        return x

    valid_grammar = set('abcdefghijklmnopqrstuvwxyz0123456789_')

    for ch in strParam:
        if ch.lower() not in valid_grammar:
            return x

    return y

TC1 = str(input())
print(UsernameValidation(TC1))

