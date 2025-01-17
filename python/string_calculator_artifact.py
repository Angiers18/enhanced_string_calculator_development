"""
This module contains the logic for the string calculator and is represented by two functions:

clean_string = responsible for returning only a string of 
positive or negative numbers without any other characters.

add = responsible for adding only positive numbers less than 1000. 
If the number is greater than 1000, it is ignored, and if the number is 
negative, it throws an error.

"""

def clean_string(input_str):

    clean_numbers = []
    current_number = ""

    for item in input_str:

        if item.isdigit() or (item == "-" and not current_number):
            current_number += item

        elif item == "," and current_number:
            clean_numbers.append(current_number)
            current_number = ""

        elif not item.isdigit() and current_number:
            clean_numbers.append(current_number)
            current_number = ""

    if current_number:
        clean_numbers.append(current_number)

    cleaned_str = ",".join(clean_numbers)
    return cleaned_str


def add(numbers):

    if numbers == "":
        return 0

    split_numbers = numbers.split(",")
    int_numbers = [int(num) for num in split_numbers]

    if any([num > 1000 for num in int_numbers]):
        int_numbers = [num for num in int_numbers if num <= 1000]

    if any([num < 0 for num in int_numbers]):
        negative_numbers = [str(num) for num in int_numbers if num < 0]
        result = ', '.join(negative_numbers)

        raise Exception(f"negatives not allowed: {result}")

    return sum(int_numbers)
