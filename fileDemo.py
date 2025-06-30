'''# open a file
file1 = open("test.txt", "r")
# read the file
read_content = file1.read()
print(read_content)
# close the file
file1.close()
#we can use the with...open syntax
# to automatically close the file.
with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)
'''
# Python program to demonstrate
# writing to file
# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()


