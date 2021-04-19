def alpha(c):
    return c.isalpha()

def num(c):
    return c.isnumeric()

def get_non_terminal(non_terminal_type, line, i, token=""):
    if len(line) == i or not non_terminal_type(line[i]):
        return token
    else:
        return get_non_terminal(non_terminal_type, line, i + 1, token=token+line[i])

def get_token(text):
    for i in range(len(text)):
        if text[i].isalpha():
            return get_non_terminal(alpha, text, i)
        elif text[i].isnumeric():
            return get_non_terminal(num, text, i)
        elif text[i] == "<":
            if text[i + 1] == "=":
                return "<="
            else:
                pass
        elif text[i] == ">":
            if text[i + 1] == "=":
                return ">="
            else:
                pass
        elif text[i] == "=":
            if text[i + 1] == "=":
                return "=="
            else:
                pass
        else:
            return text[i]


def lex():
    with open("source.c", "r") as f:
        source = f.read()
        f.close()

    tokens = []
    while len(source) > 0:
        token = get_token(source)
        tokens.append(token)
        source = source[len(token):]

    print(tokens)

lex()
