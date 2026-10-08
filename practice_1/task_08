from datetime import date

def century_message(name, age, current_year):
    target_year = current_year + 100 - age
    return name + ", тебе исполнится 100 лет в " + str(target_year) + " году"

username = input("User insert name: ")
user_age = int(input("User insert age: "))
current_year = date.today().year

result = century_message(username, user_age, current_year)
print(result)
