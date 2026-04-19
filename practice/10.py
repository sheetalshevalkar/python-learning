#Exercise 17. Find factorial of a number
n = int(input("Enter a number: "))
f = 1
for i in range (1, n+1):
    f = f*i
print (f"factorial of {n}: {f}")