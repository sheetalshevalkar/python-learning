# Exercise 4. Calculate the sum of all numbers from 1 to N
print (" enter nu for calculation")
n = input()
num = int(n)
sum = 0
for i in range (1,num+1):
    sum = sum + i
print (f"sum of all no from 1 to n is {sum}")

sum = num * (num + 1)/2
print(f"sum of value with formula {sum}")

