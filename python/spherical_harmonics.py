import numpy as np
import cmath as c

#user provides m,n,lambda, and theta
N,M,LAM,THETA = input("Give n,m,lambda, and theta: ").split()

N = float(N)

M = float(M)

LAM = float(eval(LAM)) #evaluate numpy expressions, for example

THETA = float(eval(THETA)) #evaluate numpy expressions, for example


#Spherical Harmonics - Complex Exponential Form
def spherical_harmonics(n,m,lam,theta):
	if n < m:
		Y = 0
		print("n must be greater than or equal to m")
		return Y
		quit()
	Y_pos_m = c.exp(1j*m*lam) * Leg_poly(n,m,theta)
	Y_neg_m = c.exp(-1j*m*lam) * Leg_poly(n,m,theta) * (-1)**m
	#print("this is Y+, Y-",Y_pos_m,Y_neg_m)

	# if m >= 0:
	# 	Y = c.exp(1j*m*lam) * Leg_poly(n,m,np.cos(theta))
	# else:
	# 	Y = c.exp(-1j*m*lam) * Leg_poly(n,m,np.cos(theta)) * (-1)**m
	#defined in one line by
	# Y = ((1j)**(m+abs(m))) * ((np.math.factorial(n-abs(m))/np.math.factorial(n+abs(m)))**(0.5))*c.exp(1j*m*lam) * Leg_poly(n,m,theta)
	

	#normalization
	normaliziation = norm_const(n,m)
	Y_pos_m = normaliziation * Y_pos_m
	Y_neg_m = normaliziation * Y_neg_m
	return Y_pos_m,Y_neg_m

def norm_const(n,m):
	K = np.sqrt( ((2*n+1)/(4*np.pi)) * (np.math.factorial(n-m)/np.math.factorial(n+m)) )
	#K = K * ((-1)**m)*(dub_fact(2*n-1)/(2*m)) # fraudulent! achieved by guess and check
	print("this is K: ",K)
	return K

# Associated Legendre Polynomials
def Leg_poly(n,m,theta):
	# if n == 0:
	# 	P = 1
	# elif n == 1:
	# 	P = x
	# else:
	# 	P = (2*n-1)/n * x * Leg_poly(n-1,x) - (n-1)/n * Leg_poly(n-2,x)
	# return P
	P = ((np.sin(theta))**m) * Geg_poly(n-m,m,np.cos(theta))
	#print("Leg_poly gives me P = ",P)
	return P

# Gegenbauer Polynomials - takes floating points n,m, and x
# For spherical harmonics, associated LP is Geg_poly with m = 1/2
def Geg_poly(n,m,x): #defined recursively! Notice that geg_poly calls itself
	if m == 0: # used to be n == 1 --- something is up with recursion defn --- consult with gegC[] wolfram function
		C = 1
	elif n == 0:  #did this work??
		C = 1
	elif n == 1:
		C = 2*m*x
	else:
		C = (1/n)*(2*x*(n+m-1)*Geg_poly(n-1,m,x) - (n+(2*m)-2)*Geg_poly(n-2,m,x))
	print("Geg_poly:  Given n,m,x = ",n,m,x,", I output C = ",C)
	return C


def dub_fact(k):
	if k <= 0:
		return 1
	else:
		return k * dub_fact(k-2)





myY_pos,myY_neg = spherical_harmonics(N,M,LAM,THETA)
print("Y(n,m) = ",myY_pos)
print("Y(n,-m) = ",myY_neg)


# Notes for 10/9/17
# Something is up with the recursion relation defined by all the texts (such as wolfram website)
# n = 0, lambda free should give C = 1, but when using gegC[], it gives 0.  if instead you force lambda/m to be 1
# then it makes C = 1 as desired --- this solves some problems - then there are some division by zero errors
# does the addition of elif n == 0 work?

