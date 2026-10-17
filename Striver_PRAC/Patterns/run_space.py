age=[12,32,4,3,2,1,2,1,3,2,3,4,4,5,6,7,77,8,0,8,-2]
# def cond(x):
#     return(x<5)
above5=list(filter(bool,age))

above5.sort()
print(above5)
