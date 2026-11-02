def linear_search(arr, target):
    for index, element in enumerate(arr): 
        if element == target:              
            return index                   
    return -1                              


print(linear_search([5, 3, 7, 1, 4], 1))
print(linear_search([5, 3, 7, 1, 4], 6))
print(linear_search([1, 2, 2, 3], 2))  
print(linear_search([], 1)) 