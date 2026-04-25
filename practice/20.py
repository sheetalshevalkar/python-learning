#Exercise 26. Print full multiplication table (1 to 10)
# n=10
# for i in range(1,n+1):
#     for j in range (1,n+1):
#         print(i*j,end="  ")
#     print()


n = 10
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i*j:4}", end="")
    print()