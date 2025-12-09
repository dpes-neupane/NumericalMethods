#lab-3 Find the root of the equation f(x) = 3x-cos(x)-1 with error less than 0.001.


import math 



def f(x):
    return 3*x - math.cos(x) -1
    


def Secant(xi, xprev, itrs, eps):
    for i in range(itrs):
        fxi = f(xi)
        fxprev = f(xprev)
        print(fxi, fxprev)
        xnxt = xi - ((fxi * ( xi - xprev)) / (fxi - fxprev))
        error = abs((xnxt- xi)/xnxt) 
        print(f"The root estimate is: {xnxt:.4f} and the error is: {error:.4f}")
        if error <= eps:
            return xnxt
        else:
            xprev = xi
            xi = xnxt
    return xnxt

if __name__ == '__main__':
    print("Program to find the root of the given function using secant method.")
    xprev = float(input("Enter the initial guess:"))
    x = float(input("Enter the next initial guess:"))
    eps = float(input("Enter the error tolerance value:"))
    itr = int(input("Enter the number of iterations:"))
    root = Secant(x, xprev, itr, eps)
    print(f"The root of the function is {root:.4f}")