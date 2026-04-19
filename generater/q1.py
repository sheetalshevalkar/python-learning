print(i for i in range(5))


def gen():
    for i in range(5):
        yield i

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))