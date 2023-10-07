# Decorators are that fun. which are change the other fun. and return it.
# e.g. 1st fun. get 2nd fun. and renue 2nd fun. and return it.


# def hello():
#     print("Hello world")

# hello()


# Now we see before the run function how to run decorator.
# Decorators is fun. which take another fun. as an argument and return new fun. that modify behaviour of the original fun.

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks For using this function")
    return mfx

@greet
def hello():
    print("Hello world")

hello()