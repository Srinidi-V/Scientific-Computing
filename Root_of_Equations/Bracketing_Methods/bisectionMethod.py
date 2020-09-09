
#Function defining bisection method
def bracket(xl,xu,e):
    xh = float((xl+xu)/2)
    if abs(f(xh)) < e:
        return xh
    elif f(xl) * f(xh) < 0:
        return bracket(xl,xh,e)
    else:
        return bracket(xh,xu,e)

#Define the function whose roots are to be found
def f(x):
    return x**3-5*x-9

#Function to get inputs
def input_first():
    xl = int(input("Enter first guess: "))
    xu = int(input("Enter second guess: "))
    e = float(input("Enter error value allowed (epsilon): "))
    print(xl)
    print(xu)
    print(e)
    if f(xl) * f(xu) < 0:
        a = bracket(xl,xu,e)
        print("Root is : " + str(a))
        exit()
    else:
        input_first()

#Calling input function
input_first()
    