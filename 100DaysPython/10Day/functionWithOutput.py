def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Please enter your first or last name"
    else:
        return f_name.title() + " " + l_name.title()


#title_name = format_name("aLeX", "AciKGOZ")

#print(format_name("ramAzan", "AcIkgOz"))
#print(title_name)

print(format_name(input("What is your first name? "), input("What is your last name? ")))
