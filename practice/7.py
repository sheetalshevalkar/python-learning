#Exercise 14. Reverse an integer number
number = 12345
reversed_number = 0

while number > 0:
    digit = number % 10 # Get the last digit of the number
    reversed_number = (reversed_number * 10) + digit #
    number //= 10 # Remove the last digit from the number

print("Reversed number:", reversed_number)



