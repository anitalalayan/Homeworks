def make_config(key, value):
    def custom_dict():
        return dict(eval(key) = value)
    return custom_dict


key = input("Enter a key for your dictionary: ")
value = input(f"Enter a value for your {key}: ")

res = make_config(key, value)

print(res())
