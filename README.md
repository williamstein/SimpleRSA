SimpleRSA
=========

 This program is a class model for generating a simple public-key encryption using 	the RSA model
 The algorithm uses Karatsuba's algorithm for multiplying two big integers in O(n^1.585) runtime as
 opposed to the naive method of O(n^2) multiplication.
 
 Multiplying big integers guarantes producing secure public-key and private-key
 
 The program then produces individual integers in the range [limit, 2*limit] to make up the
 modulus of the public-key
 
 
 The private-key is generted using Euclidean's Greatest Common Divisor method. 
 
 The class also contains a method to generate primes using the Sieve of Atkins algorithm. Since for now
 we only use two randomly chosen large integers, this algorithm is not used to generate the modulus of
 the public-key
 
 
 To test it , create an object of type SimpleRSA and give it a paramter specifying the size of integers
 that make the modulus of your public key. If nothing is specified, the program usses Python 3.2x 
 sys.maxsize to initliaze limit. Hence, the resulting public-key, private-key are big numbers,

Then call the method `````Python compute()````` on that object 

Following are some examples:

`````Python
>>> import SimpleRSA
>>> enc =SimpleRSA.SimpleRSA(23)
>>> enc.compute()

public key (1472, 29)
private key (1472, 914)


>>> enc =SimpleRSA.SimpleRSA() 
>>> enc.compute()
public key (10468427810168432640, 9554926832143394029)
private key (10468427810168432640, 15581655766859127013)

`````

Notice that, in the third example, we do not supply an upper bound for indiividual integers that make the public 
and private key. In this case, the program simply uses `````Python sys.maxsize````` which is equal to 2147483647


