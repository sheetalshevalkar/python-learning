#Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
n = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for i in range (len(n)):
    if n[i]%2 == 0:
        even.append(n[i])
    else:
        odd.append(n[i])
print(even+odd)