def myfunc(func):
    def f():
        print(f"executing {func.__name__}...")
        func()
    return f

@myfunc
def hello():
    msg = "new message"
    print("hello world!")

hello()