def outer():

    def inner():
        print("Hello")

    return inner #return inner function not inner function call


f = outer() # inner fuction assignment to f
f()  # inner() function call

'''
outer() run 
   ↓
def inner():   → inner function create 
   ↓
inner return hua → inner function ko outer function return kar diya Important point ⚡inner () -nahi inner fuction return hua
 Matlab:
function call nahi
function return
Ab memory me:
     ↓
f = inner

'''