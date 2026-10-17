n=5
def rev_left_triangle_fun(n=5)->None:
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
rev_left_triangle_fun()
        
def rev_left_num_triangle_fun(n=5)->None:
    for i in range(0,n):
        for j in range(1,n-i+1):
            print(j,end=" ")
        print()
rev_left_num_triangle_fun()