def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

user_a = float(input("User insert a:"))
user_b = float(input("User insert b:"))

result_a, result_b = swap(user_a, user_b)
print("Result a:", result_a)
print("Result b:", result_b)