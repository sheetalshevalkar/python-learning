def d1(func):               # Step 2: d1 ko ek function milega
                            # yaha func = result of d2(hello)

    def wrapper():          # Step 3: wrapper1 create hota hai
        print("1")          # Step 6
        func()              # Step 7: yaha d2 ka wrapper run hoga
        print("2")          # Step 10

    return wrapper          # Step 4: wrapper1 return


def d2(func):               # Step 2: d2 ko original hello function milega
                            # yaha func = hello

    def wrapper():          # Step 3: wrapper2 create hota hai
        print("3")          # Step 8
        func()              # Step 9: original hello() run hoga
        print("4")          # Step 10

    return wrapper          # Step 4: wrapper2 return


@d1
@d2
def hello():                # Step 1: original function create hota hai
    print("Hello")


# Python internally ye karta hai:
# Step 1
# hello = d1(d2(hello))

# Breakdown:
# Step A → d2(hello) run hota hai → wrapper2 return
# Step B → d1(wrapper2) run hota hai → wrapper1 return
# Step C → hello = wrapper1


hello()                     # Step 5: hello() call

# Actual execution flow:

# wrapper1() run
# print("1")

# func() → wrapper2() run
# print("3")

# func() → original hello()
# print("Hello")

# print("4")

# print("2")