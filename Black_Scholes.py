import numpy as np
import time

####   DEDOMENA

S0=97
K=103
T=1.5
r=0.05
σ=0.2


N1=100
print("Για τα ερωτήματα 1-4 θέτω N1=",N1,'\n')

####   ERWTIMA 1o
print("Απάντηση 1ου ερωτήματος: \n")
print("Για N =",N1," έχουμε τις παρακάτω ψευδοτυχαίες z τιμές : \n")
z=np.random.standard_normal(N1)
print(z,'\n')

####  ERWTIMA 2o
print("Απάντηση 2ου ερωτήματος: \n")   
St=S0*np.exp((r-(1/2)*(σ**2))*T + σ*np.sqrt(T)*z)
print ("Ο δείκτης λήξης για κάθε ψευδοτυχαίο αριθμό: \n\n",St,'\n')

####  ERWTIMA 3o
print("Απάντηση 3ου ερωτήματος: \n")   
HT = np.maximum(St - K , 0)
print("Όλες οι ενδιάμεσες τιμές: \n\n",HT,'\n')
print('\n')

####  ERWTIMA 4o
print("Απάντηση 4ου ερωτήματος: \n")   
C0 = np.exp(-r*T)*np.mean(HT) 
print("Επομένως για Ν =100 η τρέχουσα αξία ισούται με Co =",(round(C0,5)))
print('\n')

###### A + B ERWTHMATA
print("Απάντηση Α+Β ερωτήματος: \n")  
t0 = time.time()
for N in [10**3,10**5,10**7] :
    z=np.random.standard_normal(N)
    St=S0*np.exp((r-(1/2)*(σ**2))*T + σ*np.sqrt(T)*z)
    HT = np.maximum(St - K , 0)
    C0 = np.exp(-r*T)*np.mean(HT)
    t1 = time.time()
    total = t1-t0
    print("Για N=",N,"η τρέχουσα αξία είναι C0=",C0,"και το πρόγραμμα για τον υπολογισμό της απαιτεί για να κατασκευαστεί ",total,"δευτερόλεπτα")
    
