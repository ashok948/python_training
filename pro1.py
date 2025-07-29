from sympy.vector import *
from sympy import symbols
N=CoordSys3D('n')
x,y,z=symbols('x y z')
A=N.x**2*N.y+2*N.x*N.z-4
delop=Del()
print(delop(A))
gradA=gradient(A)
print(f"\n Gradient{A}is \n")
print(gradA)