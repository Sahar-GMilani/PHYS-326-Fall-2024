0import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
plt.style.use('default')
plt.rcParams.update({'font.size': 14})

#%% Functions
#-----------------------------------------------------------------------------------------------------------------------
def integrand_g(alpha, u, v):
    return (u - v*np.cos(alpha))**(-3/2)
def g_func(u, v):
    return quad(integrand_g, 0, 2*np.pi, args=(u, v))[0]

def integrand_h(alpha, u, v):
    return integrand_g(alpha, u, v)*np.cos(alpha)

def h_func(u, v):
    return quad(integrand_h, 0, 2*np.pi, args=(u, v))[0]

def u_func(s_R, z_R):
    return 1 + (s_R)**2 + (z_R)**2

def v_func(s_R):
    return 2*s_R

def Es_func(s_R, z_R):
    u = u_func(s_R, z_R)
    v = v_func(s_R)
    return s_R*g_func(u, v) - h_func(u, v)
def Ez_func(s_R, z_R):
    u = u_func(s_R, z_R)
    v = v_func(s_R)
    return z_R*g_func(u, v)
#%% Plotting
#ranges
s_R_min = 0
s_R_max = 4
z_R = 0
nPoints = 1000
#axes
s_R = np.linspace(s_R_min, s_R_max, nPoints)
Es = np.vectorize(Es_func)(s_R, z_R)
Ez = np.vectorize(Ez_func)(s_R, z_R)
#plots
plt.plot(s_R, Es)
plt.xlabel('s/R')
plt.ylabel(r'$(4\pi\epsilon_{0} R / \lambda)E_{s}$')
plt.title('$s$-component of electric field for $z/R={}$'.format(z_R))

plt.show()

plt.plot(s_R, Ez)
plt.xlabel('s/R')
plt.ylabel(r'$(4\pi\epsilon_{0} R / \lambda)E_{z}$')
plt.title('$z$-component of electric field for $z/R={}$'.format(z_R))

plt.show()

