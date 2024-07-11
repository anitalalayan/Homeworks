file = open('specific_position.txt', 'w')
file.write("Errors are my inseperable companions.\n")
file.close()



myfile = open('specific_position.txt', 'r+')
myfile.seek(15)
myfile.write("New text inserted at specific position.\n")

myfile.seek(0)
content = myfile.read()

print(content)

myfile.close()
