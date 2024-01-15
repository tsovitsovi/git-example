def month_to_season(month_number):
    if month_number in [12, 1, 2]:
        return "зима"
    elif month_number in [3, 4, 5]:
        return "весна"
    elif month_number in [6, 7, 8]:
        return "лето"
    elif month_number in [9, 10, 11]:
        return "осень"
    else:
        return "Такого месяца не существует"

print(month_to_season(10)) 
