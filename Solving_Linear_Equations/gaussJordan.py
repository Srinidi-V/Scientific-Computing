import numpy as np

#Function to implement gauss jordan
def gauss_jordan(a,n):
    x = elimination(a,n)
    print("Final")
    print(a)
    if x!=-1:
        print("Singular matrix")
        if a[x,n]!=0:
            print("Inconsistent solution")
        else:
            print("Infinite solutions")
    back_substitution(a,n)

#Function to perform elimination
def elimination(a,n):
    for k in range(n):
        for i in range(n):
            if i!=k:
                r = a[i,k]/a[k,k]
                for j in range(n+1):
                    if j!=k:
                        a[i,j] = a[i,j]-a[k,j]*r
                a[i,k]=0
        print(a)
    return -1

#Function to perform backward substitution and find the x values
def back_substitution(a,n):
    solution = np.zeros((n))
    for i in range(n-1,-1,-1):
        solution[i]=a[i,n]
        solution[i] = solution[i]/a[i,i]
    print(solution)
 
#Taking user input of the size of square matrix
n=int(input("Number of rows (=columns) : "))

#Initialising the augmented matrix for AX=B
a= np.zeros((n,n+1))

#User input of Augmented matrix entries
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = int(input( 'a['+str(i)+']['+ str(j)+']='))

gauss_jordan(a,n)