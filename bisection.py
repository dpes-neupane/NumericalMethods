import math 



def fx(x):
    return x**2 - 4 * math.sin(x)


def bisection(xu, xl, eps, itr):
    for i in range(itr):
        f_u = fx(xu)
        f_l = fx(xl)
        if f_u * f_l > 0:
            return "Root does not exist in the initial guess values. Please try other guesses."
        else:
            xm = (xu + xl) / 2
            f_m = fx(xm)
            if f_l * f_m < 0:
                xu = xm
                f_u = f_m
            else: 
                xl = xm
                f_l = f_m
            error = abs((xu - xl) / xu )
            if  error < eps: 
                return (xu+xl) / 2
        print(f"The error in the {i+1} iteration is: {error:.3f} and xu={xu:.3f}, xl={xl:.3f} and xm={xm:.3f}.")
    return xm


if __name__ == "__main__":
    print("Program to return the root of the function using the bisection method.")
    xl = float(input("Enter the value of x_l (lower bracket)"))
    xu = float(input("Enter the value of x_u (upper bracket)"))
    eps = float(input("Enter the value of error tolerance."))
    itr = int(input("Enter the number of iterations:"))
    root = bisection(xu, xl, eps, itr)
    if isinstance(root,str):
        print(root)
    else:
        print(f"The value of the root is {root:.3f}")