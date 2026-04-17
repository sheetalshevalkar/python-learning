# Exercise 4. Calculate the sum of all numbers from 1 to N

# num= int(input(print (" Enter num ")))
sum=0
n = int(input("Enter a number: "))
while n > 0:
    sum += n
    n= n - 1
print (f"sum is {sum}")