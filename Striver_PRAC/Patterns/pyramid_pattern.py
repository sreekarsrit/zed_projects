def pyramid_pattern(n=5)->None:
    for i in range(n):
        # space
        for j in range(0,n-i-1):
            print(" ",end=" ")
        for j in range(0,2*i+1):
            print("*",end=" ")
        # space
        # for j in range(0,n-i-1):
            # print(" ",end=" ")
        print()
# pyramid_pattern()

def rev_pyramid_pattern(n=5)->None:
    for i in range(n):
        # space
        for j in range(i):
            print(" ",end=" ")
        #stars
        for j in range(n*2-(2*i+1)):
            print("*",end=" ")
        # space
        # for j in range(i):
        #     print(" ",end=" ")
        print()

# diamond_pattern
pyramid_pattern()
rev_pyramid_pattern()

