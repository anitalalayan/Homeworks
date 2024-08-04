def read_file(file_name):
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    return content

def write_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()

def append_file(file_name, content):
    file = open(file_name, 'a')
    file.write(content)
    file.close()

def delete_file(file_name):
    file = open(file_name, 'w')
    file.truncate()  # Truncate the file to delete its content, only method i could find
    file.close()

    file_operations = {
    'read': read_file,
    'write': write_file,
    'append': append_file,
    'delete': delete_file
}

def file_manager(file_name, operation, **kwargs):
    return file_operations.get(operation)(**kwargs)

file_name = 'example.txt'


file_manager(file_name, 'write', content='Hello, world!')
print(f"Content written to {file_name}.")

content = file_manager(file_name, 'read')
print(f"Content read from {file_name}: {content}")

file_manager(file_name, 'append', content='\nWhat a beautiful day!.')
print(f"Content appended to {file_name}.")

file_manager(file_name, 'delete')
print(f"Content deleted from {file_name}.")

