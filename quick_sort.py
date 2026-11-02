def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    pivot = arr[mid]
    
    left = [x for i, x in enumerate(arr) if x <= pivot and i != mid]
    right = [x for i, x in enumerate(arr) if x > pivot and i != mid]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([4, 2, 7, 1, 3, 5]))
print(quick_sort([7, 3, 3, 4, 1]))
print(quick_sort([]))