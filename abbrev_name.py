def abbrev_name(first_name, last_name):

    name_initials = first_name[0].upper() + "." + last_name[0].upper()
    
    return name_initials

first_name = input("write your first name: ")

last_name = input("write your last name:")

answer = abbrev_name(first_name, last_name)
print(answer)