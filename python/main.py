from string_calculator_artifact import add, clean_string


def calculator(string):

    try:

        cleaned_str = clean_string(string)
        sum_result = add(cleaned_str)
        return sum_result

    except Exception as e:

        return f"Exception {e}"

if __name__ == '__main__':
    calculator(string=str)
