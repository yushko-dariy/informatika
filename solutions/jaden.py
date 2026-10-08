def to_jaden_case(text):
    return " ".join(word.capitalize() for word in text.split(" "))

a = input("User insert a: ")
print("Result:", to_jaden_case(a))