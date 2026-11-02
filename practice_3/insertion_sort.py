def insertion_sort(arr):
    new_arr = arr.copy()
    for i in range(1, len(new_arr)):
        key = new_arr[i]
        j = i - 1
        while j >= 0 and new_arr[j] > key:
            new_arr[j + 1] = new_arr[j]
            j -= 1
        new_arr[j + 1] = key
    return new_arr

print(insertion_sort([4, 2, 7, 1, 3, 5]))
print(insertion_sort([7, 3, 3, 4, 1]))
print(insertion_sort([])) 