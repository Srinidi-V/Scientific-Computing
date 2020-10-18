import numpy as np

#Function implementing power method
def PowerMethod(n,a,x,e,max_itr):
    l_o = 1.0
    flag = 0
    cnt = 0
    while flag!=1:
        x = a@x
        l_n = max(abs(x))
        x = x/l_n
        print("Iteration " + str(cnt+1) +":\n")
        print("x: " + str(x) + "\tnew lambda: " + str(l_n))
        cnt = cnt + 1
        if cnt>max_itr:
            print("Cant converge!")
            break
        if abs(l_o - l_n)<e:
            flag = 1
            l_o = l_n
        else:
            l_o = l_n
    return l_o
            
#Getting user inputs
 
n = int(input("Enter the size of the matrix:"))
a = np.zeros((n,n))

print("Enter the matrix A values: ")
for i in range(n):
    for j in range(n):
        m = float(input("Enter a[" + str(i) + "," + str(j) + "]:"))
        a[i,j]=m

e = float(input("Enter the allowed error value: "))

x = np.zeros(n)
print("\nEnter values for initial guess:")
for i in range(n):
    m = float(input("Enter x[" + str(i) + "]:"))
    x[i] = m
    
max_itr = int(input("Enter the number of maximum iterations: "))

#To find smallest eigen value of the matrix A, we find the largest eigen value of matrix A_inverse using power method
a_inv = np.linalg.inv(a)

big_l=PowerMethod(n,a_inv,x,e,max_itr)

#Inverting the obtained eigen value to get smallest eigen value of A
final_l = 1/big_l

print("Smallest eigen value for A: " + str(final_l))