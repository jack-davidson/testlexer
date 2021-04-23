def num(c):
    return c.isnumeric()


def alpha(c):
    return c.isalpha()


def get_non_terminal(token_type, source, i, token=""):
    if len(source) == i or not token_type(source[i]):
        return token
    else:
        return get_non_terminal(token_type, source, i + 1,
                                token=token+source[i])


# TODO: make literals/identifiers use any combo of letters, can
# be later recognized by scanner

# Create tokens from source source
def lex(source):
    tokens = []
    i = 0
    string_literal = False
    while i < len(source):
        if source[i] == "\"":
            if string_literal:
                tokens[-1] += "\""
                string_literal = not string_literal
            else:
                tokens.append("\"")
                string_literal = not string_literal
        elif string_literal:
            print(source[i])
        elif source[i].isalpha():
            # Get first alpha token from buffer of following characters.
            # The size of this buffer is decides the maximum token size.
            token = get_non_terminal(alpha, source[:64], i)
            tokens.append(token)
            # Set source index to next token.
            i += len(token) - 1
        elif source[i].isnumeric():
            # Get first numeric token from buffer of following characters.
            # The size of this buffer is decides the maximum token size.
            token = get_non_terminal(num, source[:64], i)
            tokens.append(token)
            i += len(token) - 1
        elif source[i] == "<":
            if source[i + 1] == "=":
                tokens.append("<=")
            else:
                pass
        elif source[i] == ">":
            if source[i + 1] == "=":
                tokens.append(">=")
            else:
                pass
        elif source[i] == "=":
            if source[i + 1] == "=":
                tokens.append("==")
            else:
                pass
        else:
            tokens.append(source[i])
        i += 1
    return tokens


with open("source.c", "r") as f:
    source = f.read()
    f.close()

print(lex(source))
