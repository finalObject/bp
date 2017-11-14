import matplotlib.pyplot as plt
from sympy import *
x=Symbol('x')
result = diff(x**2,x)
num = result.subs(x,1)
x=[]
plt.plot(x, b, label='x', color="green", linewidth=1)