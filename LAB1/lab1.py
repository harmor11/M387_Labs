import numpy as np
import matplotlib.pyplot as plt
import random as rn

def expser(n,x,eps=0):
#truncated Maclaurin series (i.e., Taylor polynomial) for exp
# n - degree of the Taylor polynomial
# x - the argument
# eps - relative error in computation of the series terms, modeled by uniform noise
    b=1.
    y=b
    for i in range(1,n+1):
        b*=float(x)/i
        r=2*eps*rn.random()-eps
        y+=b*(1.+r)
    return y

def expserlist(n,xlist,eps=0):
#works with *list* of x
    ylist = []
    for x in xlist:
        ylist.append(expser(n,x,eps))
    return ylist

def errelist(n,x,elist):
#difference between Tn(x) and e^x
#works with *list* of eps
    yy = []
    for eps in elist:
        yy.append(expser(n,x,eps)-np.exp(x))
    return yy

def errxlist(n,xlist,eps):
#difference between Tn(x) and e^x
#works with *list* of x
    yy = []
    for x in xlist:
        yy.append(expser(n,x,eps)-np.exp(x))
    return yy

def errnlist(nlist,x,eps):
#difference between Tn(x) and e^x
#works with *list* of n
    yy = []
    for n in nlist:
        yy.append(expser(n,x,eps)-np.exp(x))
    return yy

# xlist = np.linspace(-12, 12, 500)
# nlist = [500]
# elist = [.1, .2, .3, .4, .5]
# eps=.1
# kmax=30
#
# fig = plt.figure(figsize=(10,10))
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)
#
# ax1.plot(xlist,np.exp(xlist),label='exact')
# for e in elist:
#     for n in nlist:
#         ax1.plot(xlist,expserlist(n,xlist,e),label='n=%d'%n)
#     plt.legend()
#     for n in nlist:
#         y=np.abs(errxlist(n,xlist,e))
#         for k in range(1,kmax):
#             z=np.abs(errxlist(n,xlist,e))
#             y=np.maximum(y,z)
#         ax2.plot(xlist,y,label='n=%d'%n)
#
# ax1.set_title(r'$e^x$ and and its Taylor polynomials (machine $\varepsilon$=%.2f)'%eps)
# ax1.xaxis.set_label_coords(.5,.06)
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.legend(loc="upper center")
# ax2.set_title(r'error of Taylor polynomials (machine $\varepsilon$=%.2f)'%eps)
# ax2.set_xlabel('x')
# ax2.set_ylabel('error')
# ax2.legend(loc="upper center")
# plt.yscale('log')
# plt.show()

nlist = [3,4,9, 100]
elist = np.logspace(-3, .5, 550)
x=2.
kmax=20

plt.figure(figsize=(10,5))
for n in nlist:
   y=np.abs(errelist(n,x,elist))
   for k in range(1,kmax):
       z=np.abs(errelist(n,x,elist))
       y=np.maximum(y,z)
   plt.plot(elist,y,label='n=%d'%n)

plt.xscale('log')
plt.yscale('log')
plt.title(r'total error vs machine $\varepsilon$, at x=%.1f, for various n'%x)
plt.xlabel(r'machine $\varepsilon$')
plt.ylabel('error')
plt.legend()
plt.show()

# xlist = range(1, 10)
# nlist=range(1,30)
# eps=.1
# kmax=20
#
# plt.figure(figsize=(10,5))
# for x in xlist:
#     y=np.abs(errnlist(nlist,x,eps))
#     for k in range(1,kmax):
#         z=np.abs(errnlist(nlist,x,eps))
#         y=np.maximum(y,z)
#     plt.plot(nlist,y,label='x=%.1f'%x)
#
# plt.yscale('log')
# #plt.xscale('log')
# plt.title(r'total error vs polynomial degree, at various x (machine $\varepsilon$=%.2f)'%eps)
# plt.xlabel('Taylor polynomial degree n')
# plt.ylabel('error')
# plt.legend()
# plt.show()
