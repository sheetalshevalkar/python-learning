#Exercise 16. Check if a number is a palindrome
number = 1213
temp = number
reverse_no = 0 
while number > 0:
    digit = number%10
    reverse_no = (reverse_no*10) + digit
    number = number//10

if reverse_no == temp:
 print ( f" no {temp} is palindrome")
else :
   print ( f" no {temp} is not palindrome")

# shorter version
num = 121
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")