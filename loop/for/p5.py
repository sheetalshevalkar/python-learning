 #Create a program that takes an integer and prints its multiplication table from 1 to 10.

num = int(input("Enter no for multiplication table: "))
mul= 0
for i in range (1, num+1):
    mul = num * i
    print (f"{num} x {i} = {mul}")

