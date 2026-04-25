#Exercise 30. Remove duplicates without set
l = [1, 2, 2, 3, 4, 4, 4, 5]
r = []
for i in range (len(l)):
    if l[i] not in r:
        temp = l[i]
        r.append(l[i])
print (r)