def unique_in_order(sequence):
    if not sequence:
        return []
        
    result = [sequence[0]]
    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)
            
    return result

print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order("ABBCcAD"))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order(""))