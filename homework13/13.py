reserved_names = ['root', 'admin', 'developer', 'support']
username = input("Please enter a valid username: ")

if len(username) >= 5 and len(username) <= 20 and username.isalnum() and username.lower() not in reserved_names:
    print("Username is valid")

elif len(username) < 5 or len(username) > 20:
    print("Username should be between 5 and 20 characters long.")
elif not username.isalnum():
    print("Username can only contain alphanumeric characters.")
elif username.lower() in reserved_names:
    print("Username is a reserved name.")



email = input("Please enter a valid emeil: ")

if '@' in email and '.' in email:
    main_part, domain_part = email.split('@', 1)      # splitting as soon as the first @ is met
    
    if main_part and domain_part:
       
        if '.' in main_part and not main_part.startswith('.') and not main_part.endswith('.'):
            print(f"The email '{email}' is valid.")
        else:
            print(f"The email '{email}' is not valid.")

else:
    print(f"The email '{email}' is not valid.")



phonenumber = input("PLease enter a valid phonenumber: ")

if phonenumber.startswith('+') and phonenumber[1:].isdigit() or phonenumber.startswith('0') and phonenumber[1:].isdigit():
        
    print(f"{phonenumber}: Valid")

else:
    print(f"{phonenumber}: Invalid")



password = input("Please enter a strong password: ")

password_repeat = input("Repeat your password: ")


if password_repeat == password:
    if len(password) < 8:
        print("Invalid password. Password must be at least 8 characters long.")

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*"


    for char in password:
        if 'a' <= char <= 'z':      #or built-in methods (islower,isdigit,isupper)
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_characters:
            has_special = True

    if len(password) >= 8 and has_lower and has_upper and has_digit and has_special:
        print("Valid password")

    else:
        print("Invalid passsword: Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).") 

else:
    print("Passwords do not match. Try again.")
