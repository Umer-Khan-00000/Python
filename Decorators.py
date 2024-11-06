def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this ...")
    return mfx

@greet
def hello():
    print("Hello, World!")

def add(a, b):
    print(a + b)

hello() 