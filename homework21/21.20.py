def read_file(file_name):
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    return content
    

def write_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()
    return f"Content written to {file_name}."

def append_to_file(file_name, content):
    file = open(file_name, 'a')
    file.write(content)
    file.close()
    return f"Content appended to {file_name}."

def delete_file(file_name):
    file = open(file_name, 'r+')
    file.truncate(0)
    file.close()
    return f"{file_name} has been 'deleted' (truncated)."

file_operations = {
    'read': read_file,
    'write': write_file,
    'append': append_to_file,
    'delete': delete_file
}

def file_manager(file_name, operation, content=None):
    operation_func = file_operations.get(operation)
    
    if operation_func:
        if operation == 'delete':
            return operation_func(file_name)
        elif content is not None:
            return operation_func(file_name, content)
        else:
            return operation_func(file_name)
    else:
        return "Operation not supported."

print(file_manager('example.txt', 'write', 'Python sometimes is complicated.'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'append', '\nSure it is.'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'delete'))
print(file_manager('example.txt', 'read'))
