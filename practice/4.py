#Reverse a string using a for loop (no slicing)
input_string = "Python"
new_string = ''

for i in range(len(input_string)-1,-1,-1):
    print (i)
    new_string = new_string+ input_string[i]

print(f"new string is : {new_string}")