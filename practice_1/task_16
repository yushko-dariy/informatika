def month_calendar(start_weekday, days):
    cells = ["  "] * start_weekday

    for d in range(1, days + 1):
        if d < 10:
            cells.append(" " + str(d))
        else:
            cells.append(str(d))

    weeks = []
    for i in range(0, len(cells), 7):
        week = cells[i : i + 7]
        weeks.append(" ".join(week))

    return "\n".join(weeks)

w = int(input("User insert weekday: "))
d = int(input("User insert days: "))

result = month_calendar(w, d)
print(result)
