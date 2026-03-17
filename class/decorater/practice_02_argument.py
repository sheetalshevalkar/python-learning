def d(func): #func =mul step 2

    def wrapper(*args): #step 3
        print("Start")
        result = func(*args)
        print("End")
        return result

    return wrapper


@d
def mul(a, b):
    return a * b


print(mul(2, 3))  #==> Start, End, 6