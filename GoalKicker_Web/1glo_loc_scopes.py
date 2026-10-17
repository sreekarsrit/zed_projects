
foo = 0  # global foo
def f1():
    foo = 1  # a new foo local in f1
   
    def f2():
        foo = 2  # a new foo local in f2
       
        def f3():
            foo = 3  # a new foo local in f3
            print(foo)  # 3
            foo = 30  # modifies local foo in f3 only
       
        def f4():
            global foo
            print(foo)  # 0
            foo = 100  # modifies global foo


f1()
