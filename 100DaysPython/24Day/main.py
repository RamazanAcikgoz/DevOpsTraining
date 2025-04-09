# Open a file in python

file = open(" my_file.txt")
contents = file.read()
print(contents)
# We have to close the file
# Once python open this file it takes some resources of computer
file.close()

# Because it is kinda hard to remember to close a file
#
# WITH Keyword
# We don't have to remember to close a file
with open("second_file.txt") as file_two:
    context_second = file_two.read()
    print(context_second)

# WRITE method
# We should add mode for the file "mode = w(write)"
# It will delete old text and replace with new one
with open(" my_file.txt", mode= "a") as file:
    file.write("\nNew text")
# If we don't want to lost old text then we should use "a"(append)
# NOTE : If the giving file name is not exist then it will create a new file with this name