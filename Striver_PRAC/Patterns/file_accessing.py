# b=0
try:
    a=b
    c=a/b
except (NameError,ZeroDivisionError) as ex:
    print(ex,"error")
    
# except ZeroDivisionError as ex1:
#     print(ex1)
