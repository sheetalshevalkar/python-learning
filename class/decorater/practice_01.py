def api1():
    print("Auth check")
    print("Logging")
    print("Actual work")

def api2():
    print("Auth check")
    print("Logging")
    print("Actual work")

def common(func):

    def wrapper():
        print("Auth check")
        print("Logging")
        func()

    return wrapper

@common
def api1():
    print("API 1 work")

@common
def api2():
    print("API 2 work")

api2()