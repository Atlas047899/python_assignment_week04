def reverse_string(x):
    x = sorted(x,reverse=True)
    xword = ''.join(x)
    return(xword)

def capitalize_string(x):
    numx = len(x)
    xsplit = []
    for i in range(numx):
        if i == 0:
            xsplit.append(x[i].upper())
        else:
            xsplit.append(x[i])
    xsplit = ''.join(xsplit)
    return(xsplit)

def lowercase_string(x):
    y = x.lower()
    return(y)

def uppercase_string(x):
    y = x.upper()
    return(y)

if __name__ == "__main__":
    print(reverse_string("hello"))
    print(capitalize_string("hello"))
    print(lowercase_string("HELLO WORLD"))
    print(uppercase_string("hello"))