
#Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1

n = int(input(" enter no: "))
while n != 1:
    print (n)
    if n % 2 == 0:
        n = n//2
    else:
        n = (n*3) + 1

# Exercise 18: Collatz Conjecture

# n = int(input("Enter number: "))

# while n != 1:
#     print(n, end=" -> ")

#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = (n * 3) + 1

# print(1)