#Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
n = 2000
m = 3200
for i in range ( n, m+1):
    if i%7 == 0 and i%5!=0:
        print (f"{i},",end= "")


# another approach
n = 2000
m = 3200

result = []

for i in range(n, m + 1):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))

print(",".join(result))
        