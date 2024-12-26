
def add(input_str):
    
    if input_str == "":
        return 0
    
    str_split = input_str.split(",")
    verify_numbers = all( i in '012' for i in str_split)
    
    if verify_numbers is True:
        return sum([int(i) for i in str_split])
    
    return "Invalid Value"