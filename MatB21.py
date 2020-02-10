import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import scipy.special as special
import math

""" Task 1 """
def Rie_sum(f,a,b,h):
    """f is an callable function, a & b are the boundry and h is the meshsize """
    if not callable(f):
        raise KeyError("Can't compute the sum, due to the function not being callable.")
    Rie=[]
    while a<=b:
        Rie.append(f(a)*h)
        a+=h
    return sum(Rie)

def definiton(a,b,h):
    diff=[]
    y=[]
    while h>=0.001:
        full=abs(integral1(b)-Rie_sum(f,a,b,h))
        diff.append(full)
        y.append(h)
        h=h-0.00001
    plt.plot(y,diff)
    plt.title("Difference between integral and Rieman-sum")
    plt.xlabel("H")
    plt.ylabel("Difference")
    plt.xlim(0.01,0)
    plt.show()

def examination(t):
    dx=2*t
    dy=3*t**2
    return np.sqrt(dx**2+dy**2)

def arclenght(f,a,b):
    result=integrate.quad(f,-2,1)
    return max(result)
print(arclenght(examination,-2,1))

print(Rie_sum(examination,-2,1,0.0001))
def comparison():
    h=0.1
    solution=[]
    while h>=0.0000001:
        list1=(Rie_sum(examination,-2,1,h))
        list2=(arclenght(examination,-2,1))
        solution.append(abs(list1-list2))
        h=h-0.001
    plt.plot(solution)
    plt.xlabel("Number of partitions")
    plt.ylabel("Difference")
    plt.title("Riemann vs. Arclength")
    plt.show()
comparison()
""" Task 1.2 """
def f(x):
    return x**2
def integral1(x):
    return 1/3*x**3
print(Rie_sum(f,0,2,0.001))
