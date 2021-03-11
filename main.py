'''

Lab 2 Part 1

RSA Cryptosystem:

'''
import random
def sieve( listOfNums, upperBound ):
    print("Finding Primes! ")
    numToFilter = 3
    while ( numToFilter < upperBound ):
        for t in listOfNums:
            if ( t != numToFilter):
                if ( t % numToFilter ) == 0:
                    listOfNums.remove(t)
        numToFilter += 1;

listOfNums = []

upperBound = 101
for x in range(upperBound):
    if ( x == 2 ) | ( x % 2 ) == 1:
        listOfNums.append(x)

sieve( listOfNums, upperBound )

#randomly pick 2 primes then pick one the primes to be the e value
def getRSA( listOfNums, n, e ):
    num1 = random.choice( listOfNums )
    
    num2 = random.choice( listOfNums )
    n = num1 * num2
    e = num2
    print("RSA KEY: ", n, " ", e)
    
n = 0
e = 0
getRSA( listOfNums, n, e )  

    
    
    
    
    
    
    
    
    
