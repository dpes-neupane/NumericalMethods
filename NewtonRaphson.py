#lab-2 Find the root of the equation f(x) = x^3 - 2x - 5 with error less than 0.0001.
import math 



def f(x):
    return x**3 - 2 * x - 5
    
def fd(x):
    return 3*x**2 - 2 

def NewtonRaphson(xn, itrs, eps):
    for i in range(itrs):
        fxn = f(xn)
        fxnd = fd(xn)
        new_xn = xn - (fxn / fxnd)
        error = abs((new_xn - xn)/new_xn) 
        print(f"The root estimate is: {xn:.5f} and the error is: {error:.5f}")
        if error <= eps:
            return new_xn
        xn = new_xn
    return xn

if __name__ == '__main__':
    print("Program to find the root of the given function using newton raphson method.")
    x = float(input("Enter the initial guess:"))
    eps = float(input("Enter the error tolerance value:"))
    itr = int(input("Enter the number of iterations:"))
    root = NewtonRaphson(x, itr, eps)
    print(f"The root of the function is {root:.5f}")