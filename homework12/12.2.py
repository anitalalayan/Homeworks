user_list = []

user_keys = ['ID', 'First Name', 'Last Name', 'Email', 'Password', 'Phone Number']

user_count = int(input("Enter the number of users you want to add: "))


for i in range(user_count):

    user = dict.fromkeys(user_keys)
    user['ID'] = 11345 + i

    for key in user_keys[1:]:
       
        user[key] = input(f"Enter user's {key}: ")
    user_list.append(user)

print(user_list)

searched_user = input("Eneter user's first name to search: ")

for user in user_list:
    
    if user['First Name'] == searched_user:
        
        print(f"User found - {user}")
        break

    else:
        print("User not found")
  
