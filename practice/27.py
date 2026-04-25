'''
Exercise 29. Find common elements (Intersection) using loop
'''
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = []
for i in range(0,len(list_a)):
    if list_a[i] in list_b:
        result.append(list_a[i])
print (result)