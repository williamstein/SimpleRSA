'''
	Name - Abhishek Mishra
	Student id - 0934024
	Email - abhism@uw.edu
	File - SimpleRSA.py
	Instructor - William Stein
	Course - Math 480 Spring 2013
	Description: This program is a class model for generating a simple public-key encryption using
	the RSA model. 
'''
import math
from random import choice
from random import randint
import sys
import fractions

class SimpleRSA:
	debug = False
	def __init__(self, limit):
		self.limit = limit
		self.n = 0
		self.totient = 0
		self.e = 0
		self.d = 0
		
		
	'''	Main method for computing public-key and private-key	and storing
		 them as object class fields'''
	def compute(self,limit=sys.maxsize):
		p = randint(limit,2*limit)
		q = randint(limit ,2*limit)	
		self.n = int(self.karatsuba(p,q,2))
		self.totient = int(self.karatsuba(p-1,q-1,2))
		self.e = randint(2,self.totient-1)
		while (fractions.gcd(self.e,self.totient) != 1):
			self.e = randint(2,self.totient-1)
		self.d = self.modulo_mult_inverse(self.e, self.totient)
		print("public key", (self.n,self.e))
		print("private key", (self.n,self.d))

	# Method that calculates extended greatest common divisor for two integers 
	# a and b.
	def extended_gcd(self,b,a):
		x, lastx,y,lasty = 0,1,1,0
		while a!=0:
			quotient = b//a
			remainder = b%a
			if self.debug:	
				print("quotient",quotient)
				print("remainder",remainder)
			
			m = x - lastx*quotient
			n = y - lasty*quotient
			if self.debug:
				print("m = x - lastx*quotient:",x,"-",lastx,"*",quotient,"=",m)
				print("n = y = lasty*quotient: ",y,"-",lasty,"*",quotient,"=",n)
			
			b = a
			a = remainder
			if self.debug:	
				print("b = a: b =",a)
				print("a = remainder: a =",remainder)
			
			x = lastx
			y = lasty
		
			if self.debug:
				print("x = lastx: x=",lastx)
				print("y = lasty: y=",lasty)
			
			lastx = m
			lasty = n
			if self.debug:	
				print("lastx = m: lastx = ",m)
				print("lasty = n: lasty = ",n)
				print("--------------------------------------")
			
		return	(b,x,y)
	
	
	'''Method for calculating modulo multiplicative inverse of integer e given by
		the equation 
			d*e mod(phi(n)) = 1  
		where d is the modulo multiplicative inverse, e is the parameter being considered,
		and phi(n) is the totient of n (totient if n=p*q = (p-1)*(q-1) = phi(n))
	''' 
	def modulo_mult_inverse(self,e, totient):
		b,x,y = self.extended_gcd(totient, e)
		if b == 1:
			return x%totient
		return None
		
	'''	
		Uses the Karatsuba multiplication algorithm for multiplying two numbers in 
		O(n^1.585) runtime. This is much faster compared to the traditional O(n^2)
		normal multiplication method.
	'''
	def karatsuba(self,x, y,b):
		num_half_bitsX = len(str(x))/2
		num_half_bitsY = len(str(y))/2
		if num_half_bitsX < num_half_bitsY: 
			m = num_half_bitsX
		else:
			m = num_half_bitsY
		coeff = b**m	
		if min(x,y) < (b**(len(str(x)))):
			return x*y
		x1 = x / coeff
		x0 = x % (x1 * coeff)
		y1 = y / coeff
		y0 = y % (y1 * coeff)
			
		p0 = self.karatsuba(x0,y0,b)
		p2 = self.karatsuba(x1,y1,b)
		q  = self.karatsuba((x0+x1),(y0+y1),b)
		p1 = q - p0 - p2
		sum_first = self.karatsuba(p2, coeff, b) + p1
		sum_final = self.karatsuba(sum_first, coeff, b) + p0	
		return sum_final
	

	
	'''
		Use the Sieve of Atkins algorithm to calculate all the primes upto the 
		'limit' parameter. 
	'''
	def sieve_atkins(self,limit):
		result = [2,3,5]
		is_prime = [False]*(limit+1)
		factor = int(math.sqrt(limit))+1
		for x in range(1,factor):
			for y in range(1, factor):
				n = 4*(x**2)+(y**2)
				if (n <= limit) and ((n % 12 == 1) or (n % 12 == 5)):
					is_prime[n] = not is_prime[n]
				n = 3*(x**2)+(y**2)
				if (n <= limit) and ((n % 12) == 7):
					is_prime[n] = not is_prime[n]
				if x > y:
					n = 3*(x**2)-(y**2)
					if (n <= limit) and ((n % 12 == 11)):
						is_prime[n] = not is_prime[n]
		for i in range(5,factor):
			if is_prime[i]:
				jump = i**2
				for j in range(i**2, limit, jump):
					is_prime[j] = False
		for index in range(7,limit):
			if is_prime[index]:
				result.append(index)
		return result
		
		
		
		
		
		