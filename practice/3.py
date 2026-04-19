# Exercise 10. Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
l= len(list1)-1
print(list1[::-1])
list2 =[]

# with  loop
while l >= 0:
    list2.append(list1[l])
    l -= 1
print(list2)

# with for loop
list3 = []
for i in range(len(list1)-1,-1,-1):
    list3.append(list1[i])  
print(list3)

# Use the reversed() function for clean iteration
for item in reversed(list1):
    print(item)