#Exercise 13. Count total number of digits in a number
number = 1234567890
count = 0
s = str(number)
for i in s:
    count += 1
print(f"total number of digits in {number} is : {count}")



# Another way to count digits without converting to string
num = 75869
count = 0

# Keep dividing by 10 until the number reaches 0
while num != 0:
    # Floor division to remove the last digit
    num = num // 10
    # Increment the counter
    count = count + 1

print("Total digits are:", count)