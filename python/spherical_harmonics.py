# 10/11/17 signs are still off!
# set up the code so that it accepts negative m.  Turns it positive, runs the code, outputs Yneg
# Only need one outarg

import numpy as np
import cmath as c
import scipy as scipy
from scipy import special

#user provides m,n,theta, and lambda
N,M,THETA,LAM = input("Give n,m,theta, and lambda: ").split()

N = float(N)
M = abs(float(M))
THETA = float(eval(THETA)) #evaluate numpy expressions, for example
LAM = float(eval(LAM)) #evaluate numpy expressions, for example


#Spherical Harmonics - Complex Exponential Form
def spherical_harmonics(n,m,theta,lam):
	m = abs(m)
	if n < m:
		Y = float('NaN')
		print("n must be greater than or equal to m")
		return Y
		quit()


	#normalization
	norm_const = normalize(n,m)
	# Y_pos_m = c.exp(1j*m*lam) * Leg_poly(n,m,theta)
	# Y_pos_m = normaliziation * Y_pos_m

	if m >= 0:
		Y = c.exp(1j*m*lam) * Leg_poly(n,m,theta) * norm_const
	else:
		Y = c.exp(-1j*m*lam) * Leg_poly(n,m,theta) * norm_const * (-1)**m
	return Y


	# if m != 0:
	# 	Y_neg_m = c.exp(-1j*m*lam) * Leg_poly(n,m,theta) * (-1)**m
	# 	Y_neg_m = norm_const * Y_neg_m
	# else:
	# 	Y_neg_m = "No Y_negative"
	# return Y_pos_m,Y_neg_m


# Normalization
def normalize(n,m):
	K = np.sqrt( ((2*n+1)/(4*np.pi)) * (np.math.factorial(n - m)/np.math.factorial(n + m)) )
	K = K * dub_fact(2*M - 1) * (-1)**m # this is mysterious but it makes the code work!
	return K

# double factorial --- used for normalization...but why?
def dub_fact(k):
	if k <= 0:
		return 1
	else:
		return k * dub_fact(k-2)

# Associated Legendre Polynomials
def Leg_poly(n,m,theta):
	m_prime = m + 0.5 # adjust to definition in Boyd appendix A
	P = ((np.sin(theta))**m) * Geg_poly(n-m,m_prime,np.cos(theta))
	# print("Leg_poly gives me P = ",P) # used for testing
	return P


# Gegenbauer Polynomials - takes floating points n,m, and x
def Geg_poly(n,m,x): #defined recursively!
	if n == 0:
		C = 1
	elif n == 1:
		C = 2*m*x
	else:
		C = (1/n)*( 2*x*(n+m-1)*Geg_poly(n-1,m,x) - (n+(2*m)-2)*Geg_poly(n-2,m,x) )
	# print("Geg_poly:  Given n,m,x = ",n,m,x,", I output C = ",C) # used for testing
	return C






# myY = spherical_harmonics(N,M,THETA,LAM)
# print("MY ~~ Y(n,m) = ",myY)
# #print("Y(n,-m) = ",myY_neg)
# theirY= scipy.special.sph_harm(M,N,LAM,THETA)
# print("Their Y(n,m) = ",theirY)






#################################################################
#################################################################
######## TESTING / TESTING / TESTING / TESTING / TESTING ########
#################################################################
#################################################################



print("~~~~~~~~~~~~")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("~~~~~~~~~~~~")

# test a few values of my sph_harm vs scipy.special.sph_harm --- phi = lam
LAM = np.pi/4
THETA = np.pi/4
success = 0
iMax = 10
for i in range(0,iMax):
	M = -i
	N = i + 2
	myY = spherical_harmonics(N,M,THETA,LAM)
	theirY = scipy.special.sph_harm(M,N,LAM,THETA)
	print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
	print("iteration ",i)
	print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
	print("N = ",N,", M = ",M,", THETA = ",THETA,", PHI = ",LAM)
	print("mine: ",myY)
	print("theirs: ",theirY)
	if np.float32(myY.real) == np.float32(theirY.real) and np.float32(myY.imag) == np.float32(theirY.imag):
		print("Success!")
		success = success + 1
print(" ")
print('\033[1m' + str(success) + " out of " + str(iMax) + " tests were successful")
print('\033[0m')










# Notes for 10/9/17
# Something is up with the recursion relation defined by all the texts (such as wolfram website)
# n = 0, lambda free should give C = 1, but when using gegC[], it gives 0.  if instead you force lambda/m to be 1
# then it makes C = 1 as desired --- this solves some problems - then there are some division by zero errors
# does the addition of elif n == 0 work?

# Notes for 10/10/17
# check how far off the Y values are for n!=m --- I suspect it is something using dub fact
# make it a conditional! if n!=m, weight by dubfact

# Notes for 10/13/17
# nearly there --- negatives arent perfect (try 1 -1 np.pi/3 np.pi/5)



