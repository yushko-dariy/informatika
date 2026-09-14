def is_divisor(a, b):
    if a == 0:
        return False
    if b % a == 0:
        return True
    else:
        return False

user_a = int(input("User insert a:"))
user_b = int(input("User insert b:"))

result = is_divisor(user_a, user_b)
print("Result:", result)