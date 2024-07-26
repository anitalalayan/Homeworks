def print_user_profile(first_name, last_name, *, age, city):
    user_profile = {
        "First Name": first_name,
        "Last Name": last_name,
        "Age": age,
        "City": city
        }


    return user_profile


profile = print_user_profile("John", "Doe", age = 30, city = "New York")
print(profile)
