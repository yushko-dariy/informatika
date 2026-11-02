def max_gap(numbers):
    if len(numbers) < 2:
        return 0
        
    sorted_nums = sorted(numbers)
    max_diff = 0
    
    for i in range(len(sorted_nums) - 1):
        diff = sorted_nums[i + 1] - sorted_nums[i]
        if diff > max_diff:
            max_diff = diff
            
    return max_diff

print(max_gap([13, 10, 5, 2, 9]))
print(max_gap([-3, -27, -4, -2]))
print(max_gap([-54, 37, 0, 64, 640, 0, -15]))