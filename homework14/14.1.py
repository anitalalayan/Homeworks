myfile = open('append_mode.txt', 'a')
myfile.write("Python: your friendly guide to the world of programming.")

file_contents = open('append_mode.txt', 'r')
print(file_contents.read())

myfile.close()

