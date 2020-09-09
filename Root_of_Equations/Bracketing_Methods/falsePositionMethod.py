import math

#Function defining false position method
def falsePos(xl,xu,e):
    xh = float(xu - (( ( f(xu) * (xl-xu) ) / ( f(xl) - f(xu) )   )))
    if abs(f(xh)) < e:
        return xh
    elif f(xl) * f(xh) < 0:
        return falsePos(xl,xh,e)
    else:
        return falsePos(xh,xu,e)

#Define the function whose roots are to be found
def f(x):
    return x* math.exp(x) - 1

#Function to get inputs
def input_first():
    xl = int(input("Enter first guess: "))
    xu = int(input("Enter second guess: "))
    e = float(input("Enter error value allowed (epsilon): "))
    print(xl)
    print(xu)
    print(e)
    if f(xl) * f(xu) < 0:
        a = falsePos(xl,xu,e)
        print("Root is : " + str(a))
        exit()
    else:
        input_first()

#Calling input function
input_first()
    