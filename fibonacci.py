def fibonacci(a, b, how_many):
    nums = []
    nums.append(a)
    for num in range(how_many):
        
        nums.append(b)
        nums.append(a + b)
        c = a + b
        a = b
        b = a + b
        
        
    
 