
def add(input_str):

    if input_str == "":
        return 0

    try:
        str_replace = input_str.replace("\n", ",")
        str_split = str_replace.split(",")
        
        return sum([int(i) for i in str_split])


    except ValueError:
        return "Invalid Value"
