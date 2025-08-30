def fibonacci(a, b, how_many, nums):
    nums.append(a)
    for i in range(how_many):
        fibonacci(b, a + b) 
    return nums
        
fibonacci(0, 1, 11, [])
#check this solution with python editor later        
        
    
 