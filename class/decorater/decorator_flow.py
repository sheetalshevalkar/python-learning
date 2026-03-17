def my_decorator(func):   # Step 2: decorator function call hoga
                          # yaha func = hello (original function)

    def wrapper():        # Step 3: wrapper function create hota hai
                          # ye original function ko wrap karega
        print("Before")   # Step 6: sabse pehle ye chalega

        func()            # Step 7: yaha original hello() function call hota hai

        print("After")    # Step 8: hello() ke baad ye chalega

    return wrapper        # Step 4: wrapper function return ho jata hai


@my_decorator             # Step 1: Python internally ye karta hai:
                          # hello = my_decorator(hello)

def hello():              # Step 1a: original function create hota hai
    print("Hello")        # Step 7: jab func() call hoga tab ye chalega


# Ab decorator ke baad actual me ye ho chuka hai:
# hello = wrapper


hello()                   # Step 5: hello() call karte hai
                          # lekin hello ab wrapper hai
                          # isliye wrapper() run hota hai

# Execution flow:
# Step 6 → print("Before")
# Step 7 → func() → hello() → print("Hello")
# Step 8 → print("After")