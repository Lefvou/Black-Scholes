import numpy as np
import time

####   DEDOMENA

S0=97
K=103
T=1.5
r=0.05
σ=0.2


N1=100
print("For Tasks 1-4 we use N1=",N1,'\n')

####  Task 1
print("Task 1: \n")
print("For N =",N1,"\n")
z=np.random.standard_normal(N1)
print(z,'\n')

####  Task 2
print("Task 2 : \n")   
St=S0*np.exp((r-(1/2)*(σ**2))*T + σ*np.sqrt(T)*z)
print ("The respective 𝑆𝑇(𝑖) for each false-random Number: \n\n",St,'\n')

####  Task 3
print("Task 3 : \n")   
HT = np.maximum(St - K , 0)
print("All intermediate prices: \n\n",HT,'\n')
print('\n')

####  Task 4o
print("Task 4: \n")   
C0 = np.exp(-r*T)*np.mean(HT) 
print("For Ν =100, the current value of the product based on the appraiser Monte Carlo is: ",(round(C0,5)))
print('\n')

###### Task 5 and 6 
print("Task 5 and 6: \n")  
t0 = time.time()
for N in [10**3,10**5,10**7] :
    z=np.random.standard_normal(N)
    St=S0*np.exp((r-(1/2)*(σ**2))*T + σ*np.sqrt(T)*z)
    HT = np.maximum(St - K , 0)
    C0 = np.exp(-r*T)*np.mean(HT)
    t1 = time.time()
    total = t1-t0
    print("For N=",N,"the current value C0=",C0,"and the program for its calculation requires ",total," seconds to be constructed")
