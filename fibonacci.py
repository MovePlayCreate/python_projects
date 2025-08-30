def fibonacci(a, b, how_many):
    nums = []
    nums.append(a)
    for i in range(how_many):
        fibonacci(b, a + b)
        
fibonacci(0, 1, 11)
        
        
    
 