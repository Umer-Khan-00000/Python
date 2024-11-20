def greet(fx):
    print("Good Morning !")
    fx()
    # {
    #     @greet
    #     def hello():
    #     print("Hello, World!")
    # }
    print("Thanks for using this function!")
    return greet

@greet
def hello():
    print("Hello, World!")


    
