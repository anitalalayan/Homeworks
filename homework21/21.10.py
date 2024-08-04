def make_config(key, value):
    def get_config():
        return {key: value}
    return get_config

key = input("Enter the key: ")
value = input("Enter the value: ")

config = make_config(key, value)
print(config())
