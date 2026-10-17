def bow_pattern(n=5)->None:
    for i in range(1,2*n):
        stars=i
        if i>n:
            stars=2*n-i
        for j in range(stars):
            print("*",end=" ")
        print()

bow_pattern()