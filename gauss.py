import numpy as np
from copy import deepcopy

def on_zero_string(a, b, i):   
    flag = True
    for item in a[i]:
        if item != 0.0:
            flag = False
            break
    if flag:
        a = np.delete(a, i, axis=0)
        if b[i] != 0.0:
            print ("Решений нет")
            exit()
        b = np.delete(b, i)
    return a,b
    

def Gauss(a,b,x):    
        print (f"{a}\n\n{b}\n")   
        i = 1  
        while i < len(a): 
            a,b = on_zero_string(a, b, i-1)               
            if a[i-1,i-1] == 0.0:
                for k in range(i,len(a[i])):
                    if a[i-1,k] !=0.0:
                        a[:,[i-1,k]] = a[:,[k,i-1]]
                        break                                 
            for k in range(i,len(a)):
                cur_a = a[k,i-1] / a[i-1,i-1]
                for j in range(i-1,len(a[i])):
                    a[k,j] -=  a[i-1,j] * cur_a
                b[k] -= b[i-1] * cur_a 
            print (f"{a}\n\n{b}\n")              
            i +=1
        a,b = on_zero_string(a, b, len(a)-1)
        print (f"{a}\n\n{b}\n")      
        n = len(a)
        m = len(a[0]) 
        if n == m:
            for i in range(n):
                x[n-1-i] = b[n-1-i]/a[n-1-i,n-1-i]
                for j in range(n):
                    b[j] -= x[n-1-i]*a[j,n-i-1]                
            print (f"Гаусс решил: {x}")
        else:
            print (f"Решений бесконечно много:\nA = {a}\n\nB = {b}\n")
    
        

# A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
# b = np.array([8.2, 5.1, 2.0])
# x = np.array([0.0, 0.0, 0.0])

A = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 2.0, 3.0]])
b = np.array([1.0, 2.0, 3.0])
x = np.array([0.0, 0.0, 0.0])

# A = np.array([[5.1, 2.0, 1.0], [2.0, 6.0, 3.0], [1.0, 3.0, 5.0]])
# b = np.array([8.2, 5.1, 3.6])
# x = np.array([1.5, 0.5, 0.5])

# A = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 3.0],[1.0, 2.0, 1.0]])
# b = np.array([8.2, 5.1, 3.6])
# x = np.array([0.0, 0.0, 0.0])


Gauss(deepcopy(A), deepcopy(b), deepcopy(x))