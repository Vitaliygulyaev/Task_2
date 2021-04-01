import numpy as np

def get_N(): 
    n = int(input("Введите целое n (4<=N<=1000): "))
    try:
        if 4 <= n and n <= 1000:
            elements = [i for i in range(1, n**2+1)]
            return elements, n
    except:
        print(ValueError)
    
def get_matrix(elements, n):
    matrix_zeros = np.zeros((n, n))

    k = 0
    a = 0

    for i in range(a, n):
        for j in range(a, n):
            matrix_zeros[i][j] = elements[k]
            k+=1
        
        for i in range(a+1, n):
            matrix_zeros[i][j] = elements[k]
            k+=1

        for j in range(n-2, a-1, -1):
            matrix_zeros[i][j] = elements[k]
            k+=1
       
        for i in range(n-2, a, -1):
            matrix_zeros[i][j] = elements[k]
            k+=1
        a+=1
        n-=1
    print(matrix_zeros)

if __name__=="__main__":
    el, n = get_N()
    get_matrix(el, n)
    