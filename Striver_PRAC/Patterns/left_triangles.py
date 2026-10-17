n=5
def left_triangle_fun(n=3)->None:
    for i in range(0,n,1):
        for j in range(0,i+1,1):
            print("*",end=" ")
        print()
left_triangle_fun()

def num_left_triangle(n=5)->None:
    for i in range(1,n+1,1):
        for j in range(1,i+1):
            print(j ,end=' ')
        print()
# num_left_triangle(4)

def row_left_triangle(n=5)->None:
    for i in range(1,n+1,1):
        for j in range(1,i+1):
            print(i ,end=' ')
        print()
# row_left_triangle(4)