# In the name of GOD
# Mohammad Mahdi Shafighy
# Computer Science Student
# Practice 2 , Gas station computer simulation... 

# 2. Cars arrive to a gas station at random and they spend a random amount
# of fuel based on the size and the type of car. The work hours of the station
# is from 8 am to 6 pm. It is assumed that the time between car arrival
# is Exponentially distributed with mean 15 min. The amount of fuel is
# uniform distribution between 10 liters to 70 liter.
# (a) The gas station wants simulate the behavior of the station during 3 hours.
# (b) From (a) what is the average of number of arrivals per hour.
# (c) From (a), what is the average of amount of money collected per hour, given that the gas station charge 0.85 SR per Liter
# (d) What is the probability of fueling more than 15 liters in 3 hours.
# (e) Answer a,b,c,d for one full day?
# (f) From e , what is the distribution of number of arrivals in one hour?

#___________________________________________________
# solution (a):
# The behavior of the station during 3 hours : 3 * 60 (min)
import math
import random

# mean = 15 (min) , mean = 1 / lambda  => lambda = 1 / mean 
# => ' lambda = 1 / 15 ' 

# PDF = (1/15)*math.exp(-(1/15)*x)
# CDF = 1- math.exp(-(1/15)*x)

# Inverse of Continuous distribution function
# ICDF = (-15)*math.log(1-u)


# N : number of Cars, 
# Sum of time between's = 3 * 60 (min) 
# Sum = 180 
sum = 0
N=1
h=3

while (sum <= h*60):
    IRCDF=[]
    # Seed
    random.seed(123)

    for i in range(N):
        u = random.random()
        x = (-15)*math.log(1-u)
        IRCDF.append(x)
        roundx= round(x)
        # print(roundx)
        sum += roundx
    N+=1

# print(IRCDF,  len(IRCDF),   N)
print("We have "+str(N)+" Cars in "+str(h)+" hours.")

# Average number of Cars
ave =  N/3
print("The average number of arrivals per hour is "+str(ave)) 
    


