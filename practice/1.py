# Exercise 8. Count occurrences of a specific element in a list
list1 = [10, 20, 10, 30, 10, 40, 50]
print (list1)
l = len(list1)
c=0
n = int(input("Enter no to be find in list: "))
for i in range(0,l):
    if list1[i] == n:
        print (f"index of no : {i}: {list1[i]}")
        c= c+1

print (f"no of occurances of no {n} is {c}")


# using count built in fuction

occurance = list1.count(n)
print (f"no of count of no {n} is {occurance}")