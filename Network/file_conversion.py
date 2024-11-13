with open('example.yaml', 'w') as file:
    file.write("""
users:
  - id: 1
    name: Alice
    roles:
      - admin
      - editor
  - id: 2
    name: Bob
    roles:
      - viewer""")


import yaml
import json

with open('example.yaml', 'r') as file:
    fs = yaml.load(file, Loader=yaml.SafeLoader)

with open('users.json', 'w') as file:
    json.dump(fs, file)

with open('users.json', 'r') as file:
    fs = json.load(file)
    print(fs)