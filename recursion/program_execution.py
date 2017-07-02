def function1():                  
    print("function1 line 1")
    print("function1 line 2")
    print("function1 line 3")
    
def function2():
    print("function2 line 1")
    print("function2 line 2")
    print("function2 line 3")

def function3():
    print("function3 line 1")
    function2() # function3 line 2
    function1() # function3 line 3
    print("function3 line 4")
    
def test():
    function3() # test line 1

test()    #### 
