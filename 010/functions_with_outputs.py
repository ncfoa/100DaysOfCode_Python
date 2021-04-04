

# function to change the case of a name


def format_name(f_name, l_name):

    f_name = f_name.capitalize()
    l_name = l_name.capitalize()

    return f'{f_name} {l_name}'


full_name = format_name("dave", "BEIDLE")
print(full_name)
