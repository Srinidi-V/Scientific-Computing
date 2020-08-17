import numpy as np

#Function to implement gauss jacobi method
def gauss_jacobi(a,n):
    x = np.zeros((n))
    x1 = np.zeros((n))
    m = 0
    while m<1000:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += a[i,j]*x[j]
            x1[i] = a[i,n] - sum
            x1[i] = x1[i]/a[i,i]
        flag = 0
        for i in range(n):
            if abs(x1[i]-x[i])<epsilon:
                flag += 1
        m = m + 1
        x = x1
        if flag==n:
            return x

#Function to check if the matrix is diagonally dominant 
def diagonally_dominant(a,n): 
    count = 0
    for i in range(n):
        sum = 0
        for j in range(n):              
            sum += abs(a[i,j])
        sum -= abs(a[i,i])
        if abs(a[i,i]) >= sum:  
            count+=1  
    if count==n:
        return 1
    else:
        return 0

#Taking user input of the size of square matrix
n=int(input("Number of rows (=columns) : "))

#Initialising the augmented matrix for AX=B
a= np.zeros((n,n+1))

#User input of Augmented matrix entries
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = int(input( 'a['+str(i)+']['+ str(j)+']='))

#Setting out epsilon values
epsilon = 0.25

#Checking for diagonal dominance
x = diagonally_dominant(a,n)
if x==1:
    final_ans=gauss_jacobi(a,n)
    print(final_ans)
else:
    print("Cant converge since it is not diagonally dominant")