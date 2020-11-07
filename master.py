def myfunc(func):
    def f():
        print(f"executing {func.__name__}...")
        func()
    return f

@myfunc
def hello():
    "running hello function..."
    print("hello world!")

hello()