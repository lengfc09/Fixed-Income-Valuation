"""
Topic : Prototype for Kalotay Williams Fabozzi (KWF) Interest Rate Model in Python.

Source:  A Model for Valuing Bonds and Embedded Options by Andrew J. Kalotay, George O. Williams and Frank J. Fabozzi (via google)

Discussion: This is another prototype for KWF interest rate model in Python.  I did one before in R but found the source listed
above and did another prototype in Python to be converted to a function this weekend if time permits.  

Random Nothings:  I am getting distracted a little from this project because I want to write an article on CyberSecurity before
December.  CyberSecurity is the new buzzword and I wanna explore it and see what all the fuss is about and write an article about
it and never ever ever think about it again.  But writing a good article takes time to research especially if you are not an expert
in that domain and you just wanna do it on an ad hoc basis but the topic is of strategic importance to many organizations and countries
even so its worth exploring...........though no amount of measure can keep a company completely safe, the only way to stay safe is
to completely unplug but it is still important to explore the topic and the safeguards that are out there - best practices if you will.

Next we will continue with the automation of this implementation and continue with the BDT model......

"""



from __future__ import division
import sys
import math 
from scipy.optimize import fsolve


"""
Consider the information below:
Maturity            Yield_To_Maturity   Value          Spot_Rate
1 Year              3.50%               100.00         3.500%
2 Years             4.00%               100.00         4.010%
3 Years             4.50%               100.00         4.531%

Also assume that the coupon rates for the three securities shown above are 3.5%, 4.00% and 4.5% respectively.  
"""
        
r = 0.035
vol = 0.1
m = 0.03  #guess

c = 4.0

def KalotayOne(guess):
    ru = guess * math.exp(2 * vol)
    rd = guess
    N1 = (100 + c)/(1+ru)
    N2 = (100 + c)/(1+rd)
    return (0.5*((N1+c)/(1+r) + (N2+c)/(1+r))-100)
    
g = fsolve(KalotayOne,m)[0]

ru = g * math.exp(2 * vol)
rd = g

print (ru,rd)

c = 4.5


def KalotayTwo(guess):
    ruu = guess * math.exp(4 * vol)
    rud = guess * math.exp(2 * vol)
    rdd = guess
    N1 = (100 + c)/(1+ruu)
    N2 = (100 + c)/(1+rud)
    N3 = (100 + c)/(1+rdd)
    ans1 = (0.5*((N1+c)/(1+ru) + (N2+c)/(1+ru)))
    ans2 = (0.5*((N2+c)/(1+rd) + (N3+c)/(1+rd)))
    
    return (0.5*((ans1+c)/(1+r) + (ans2+c)/(1+r)) - 100)

g = fsolve(KalotayTwo,m)[0]

ruu = g * math.exp(4 * vol)
rud = g * math.exp(2 * vol)
rdd = g

print(ruu,rud,rdd)

finalRate = [[r],[ru,rd],[ruu,rud,rdd]]

finalRate2 = [list(reversed(x)) for x in finalRate]

print_lattice2(finalRate2, info = [])

"""
                 0                   1                   2
------------------|-------------------|-------------------
                                        0.0675735962549272
                    0.0497551231455638  0.0553245813499840
0.0350000000000000  0.0407360494424552  0.0452959361523965
"""

"""
Snippet - final function used to call the code automatically. Other helper functions not released.
"""
def solutionIterator(mo,nNodes,rate3,rate2):
    for x in range(1,nNodes):
        data = (x,rate3)
        mo.append(fsolve(valueCalculator2,m,args=data)[0])
        print mo
        rate2.append(rateCalculator2(mo[x],x))
        rate3 = rate2[1:]
        data = (x,rate3)
    return rate2
    
rate4 = solutionIterator(mo,nNodes,rate3,rate2)[:]




reversed_lists = [list(reversed(x)) for x in rate4]

#reversed_lists[1].reverse()

print "     "

print "---------------------------------------------------"
print "KALOTAY-WILLIAMS-FABOZZI SHORT RATE MODEL AUTOMATED"
print "---------------------------------------------------"

print_lattice2(reversed_lists, info = [])

print "     "


"""

This is the output from the function created for the Kalotay Williams Fabozzi model.  Code not released and will be featured
in a future article.  Next time we will model BDT, and we will start considering the applications of these models for instance
how we can use them to bootstrap OAS - Option Adjusted Spread and Z-Spreads etc etc.  See you next time!!
---------------------------------------------------
KALOTAY-WILLIAMS-FABOZZI SHORT RATE MODEL AUTOMATED
---------------------------------------------------

                 0                   1                   2
------------------|-------------------|-------------------
                                        0.0675735962549266
                    0.0497551231455642  0.0553245813499836
0.0350000000000000  0.0407360494424555  0.0452959361523961

"""
