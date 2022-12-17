from turtle import color
import numpy as np
#plank's law and rayleigh law cpmaprison

import numpy as np
import matplotlib.pyplot as plt

#define the value of constant
k=1.38e-23
h=6.626e-34
c=3e8

#wavelength=lam, lamda=x
x=np.linspace(0.01e-04,55e-06,1000)

#define energy dencity of rayligth jenes law
def E1(x,T):
    return 8*np.pi*k*T*x**(-4)

#define energy dencity: plank law
def E2(x,T):
    return (8*np.pi*h*c*x**(-5))/(np.exp(h*(c/(x*k*T)))-1)

plt.subplot(221)
plt.plot(x,E2(x,100),x,E2(x,200),x,E2(x,300),x,E2(x,400))
plt.xlabel("wavelength---->",color="r")
plt.ylabel("energy dencity---->",color="r",fontsize=10)
plt.ylim(0,2)
plt.title("plank law",color='black')
plt.grid()
plt.legend(["T=100K","T=200K","T=300K","T=400K"],loc="best")

plt.subplot(222)
plt.plot(x,E1(x,100),x,E1(x,200),x,E1(x,300),x,E1(x,400))
plt.xlabel("wavelength---->",color="r")
plt.ylabel("energy dencity---->",color="r",fontsize=10)
plt.ylim(0,2)
plt.title("raylagth jenes law",color='black')
plt.grid()
plt.legend(["T=100K","T=200K","T=300K","T=400K"],loc="best")

plt.subplot(223)
plt.plot(x,E1(x,200),x,E2(x,200))
plt.xlabel("wavelength---->",color="r")
plt.ylabel("energy dencity---->",color="r",fontsize=10)
plt.ylim(0,2)
plt.title("raylagth jenes vs palnk law at low temp(T=200)",color='black')
plt.grid()
plt.legend(["Raylagth jeans law ","plank law"],loc="best")

plt.subplot(224)
plt.plot(x,E1(x,400),x,E2(x,400))
plt.xlabel("wavelength---->",color="r")
plt.ylabel("energy dencity---->",color="r",fontsize=10)
plt.ylim(0,2)
plt.title("raylagth jenes vs palnk law at high temp(T=400)",color='black')
plt.grid()
plt.legend(["Raylagth jeans law ","plank law"],loc="best")

plt.show()