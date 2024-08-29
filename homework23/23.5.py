#Write a generator function read_file_lines(file_path) that reads a file line by line and yields each line. Use this generator to print each line of a file without loading the entire file into memory.



def read_file_lines(file_path):
    file = open(file_path, 'r')
    for line in file:
        yield line
    file.close()


file_path = 'example.txt'  
try:
    for line in read_file_lines(file_path):
        print(line, end='') 

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
