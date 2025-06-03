def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(1, 3))
print(add(4, 3, 2, 3, 34))
print(add())
