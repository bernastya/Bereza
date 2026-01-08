god = int(input("Введите год:"))


def is_year_leap(god):
    if (god % 4 == 0):
        print("True")
    else:
        print("False")


is_year_leap(god)

n = 2024


def is_year_leap(n):
    result = is_year_leap(n)


print(f"Год:", n, True)
