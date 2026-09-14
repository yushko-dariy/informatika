def echo_number(number):
    return "Thats the number you entered: " + str(number)
a = float(input("User insert a:"))
result = echo_number(a)
print(result)