from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    dict_birthday = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    today = date.today()

    for user in users: # перебираємо словники з днями народження
        # Змінемо кожну дату таким чином, щоб рік став поточним роком:
        user_birthday_in_this_year = today.replace(month=user["birthday"].month, day=user["birthday"].day)
        #Знайдемо різницю отриманої дати з нашою датою сьогодні:
        different = user_birthday_in_this_year - today  # дізнаємось різницю дати народження з сьогоднішньою датою
        days_this_year = different.days # дізнаємось кількість днів
        #Зробимо те саме для випадка, коли день народження в цьому році минув але може бути на наступному тижні:
        user_birthday_in_next_year = user_birthday_in_this_year.replace(year=today.year + 1)
        different_next = user_birthday_in_next_year - today
        days_next_year = different_next.days
        print(days_next_year)


        if  days_this_year in [0, 1, 2, 3, 4, 5, 6]:

            number_weekday = user_birthday_in_this_year.weekday() #визначемо номер тижня
            # в залежності від номера тижня будемо додавати імена до словника
            if number_weekday == 5 or number_weekday == 6 or number_weekday == 0:
                dict_birthday["Monday"].append(user["name"])
            elif number_weekday == 1:
                dict_birthday["Tuesday"].append(user["name"])
            elif number_weekday == 2:
                dict_birthday["Wednesday"].append(user["name"])
            elif number_weekday == 3:
                dict_birthday["Thursday"].append(user["name"])
            elif number_weekday == 4:
                dict_birthday["Friday"].append(user["name"])

        if days_next_year in [0, 1, 2, 3, 4, 5, 6]:
            number_weekday_next = user_birthday_in_next_year.weekday()
            if number_weekday_next == 5 or number_weekday_next == 6 or number_weekday_next == 0:
                dict_birthday["Monday"].append(user["name"])
            elif number_weekday_next == 1:
                dict_birthday["Tuesday"].append(user["name"])
            elif number_weekday_next == 2:
                dict_birthday["Wednesday"].append(user["name"])
            elif number_weekday_next == 3:
                dict_birthday["Thursday"].append(user["name"])
            elif number_weekday_next == 4:
                dict_birthday["Friday"].append(user["name"])

    for key, value in list(dict_birthday.items()):
        if len(value) == 0:
            del dict_birthday[key]

    if len(users) == 0:
        return {}
    result = dict_birthday
    return result




if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1981, 7, 23).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")