n = int(input("Введите номер месяца: "))


def month_to_season():

    if(1 <= n <= 3):
        print("Зима")
    elif(4 <= n <= 6):
        print("Весна")
    elif(7 <= n <= 9):
        print("Лето")
    elif(10 <= n <= 12):
        print("Осень")
    else:
        print("неверный номер месяца")


month_to_season()
