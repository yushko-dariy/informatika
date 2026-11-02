def sort_by_bits(numbers):
    return sorted(numbers, key=lambda x: (bin(x).count('1'), x))

print(sort_by_bits([7, 6, 15, 8]))
print(sort_by_bits([3, 8, 3, 6, 5, 7, 9, 1]))