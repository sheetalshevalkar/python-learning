#Exercise 6. Calculate the cube of all numbers from 1 to a given number
num = int(input("Enter a number: "))

i = 1

while i <= num:
    cube = i**3          # ya i**3
    print(f"Cube of {i} : {cube}")
    i += 1


