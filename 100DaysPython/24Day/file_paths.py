# Absolute file path
#
# /(root)
# /Work/Project/talk.ppt
#
# Relative file path
#
# if we are in working directory(current directory) and want to reach a file
# ./talk.ppt : It is relative file path
# ../report.doc : .. we coming out of current working directory
#
with open("/Users/ramaz/Desktop/test_file.txt") as file:
    contents = file.read()
    print(contents)


