__author__ = "LuisSas"

def ask_age():
    age = input("Enter your age: ")
    return int(age)

def calculate_second_from_year(age_years):
    return age_years * 365 * 24 * 60 * 60

def promt_user_and_calculate_age():
    age = ask_age()
    seconds_lived = calculate_second_from_year(age)
    print("Your age in seconds is {}".format(seconds_lived))

promt_user_and_calculate_age()
