def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum > target:
            right -= 1
        else:
            left += 1
            
    return None

print(two_sum_sorted([1, 2, 3, 4, 5], 9))
print(two_sum_sorted([1, 2, 3, 4, 5], 10))
print(two_sum_sorted([1, 3, 5, 7], 8))