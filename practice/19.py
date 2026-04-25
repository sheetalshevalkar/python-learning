#Exercise 25. Print pyramid pattern of stars
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = 10
t = int(n/2)+1
for i  in range (1, t+1):
    for j in range (1, i+1):
        print ("* ", end = " ")
    print()

for i  in range (t-1,-1,-1):
    for j in range (1, i+1):
        print ("* ", end = " ")
    print()

