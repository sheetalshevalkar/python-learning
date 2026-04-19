#Exercise 20. Print right-angled triangle Number Pattern using a Loop
n = 5
for i  in range (1, n+1):
    for j in range (1, i+1):
        print (j, end = " ")
    print()