def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n

    for i in range(n):
        seat_number = seats[i]
        guest_number = i + 1
        result[seat_number - 1] = guest_number

    return result

user_input = input("User insert values: ")
seats_list = []
for x in user_input.split():
    seats_list.append(int(x))

final_result = guests_by_seat(seats_list)
print("Result:", final_result)
