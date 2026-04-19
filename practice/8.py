# Exercise 15. Find largest and smallest digit in a number
number = 234562789015
larger_no = 0
smallest = 0
while number > 0:
    digit = number % 10
    if digit > larger_no :
        larger_no = digit
        print (larger_no)
    if digit < smallest:
        smallest = digit
        print (f"s: {smallest}")
    number = number//10

print (f"larget no: {larger_no}")
print (f"smallest no: {smallest}")
         
