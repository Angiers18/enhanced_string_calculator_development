
def add(input_str):

    if input_str == "":
        return 0

    try:
        str_split = input_str.split(",")
        return sum([int(i) for i in str_split])


    except ValueError:
        return "Invalid Value"
