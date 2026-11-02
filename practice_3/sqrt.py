def integer_square_root(n):
    if n == 0 or n == 1:
        return n
        
    left = 0
    right = n
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans

print(integer_square_root(0))
print(integer_square_root(4))
print(integer_square_root(8))
print(integer_square_root(10))
print(integer_square_root(100))
print(integer_square_root(10**12))