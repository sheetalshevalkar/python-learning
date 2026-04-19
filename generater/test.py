def numbers():
    for i in range(1000000):
        yield i
# numbers = numbers()     
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# def test():
#     yield 1
#     yield 2
#     yield 3

# g = test()

# print(next(g))
# print(next(g))




g1 = numbers()
g2 = numbers()

print(next(g1))
print(next(g1))
print(next(g2))