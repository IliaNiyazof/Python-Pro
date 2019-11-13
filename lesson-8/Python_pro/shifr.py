AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2  # заданный алфавит


def f(mc, key, op):
    key *= len(mc)
    return ''.join(([AZ[AZ.index(j) + int(key[i]) * op] for i, j in enumerate(mc)]))


def encrypt(text, key):
    return f(text, key, 1)


def decrypt(text, key):
    return f(text, key, -1)


def function1(text):
    print(encrypt(text, '2015'))


def function2(text):
    print(decrypt(text, '2015'))


function2('IRPSUFFQF')
function1('GRONSFELD')
