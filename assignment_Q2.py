# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.


def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")

        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


input_year = int(input("Enter a year:"))

is_leap(input_year)
