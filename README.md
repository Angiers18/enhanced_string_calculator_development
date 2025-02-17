# String Calculator Development

## Description
This project is an implementation of a **String Calculator** in two programming languages: **Python** and **F#**.

## Main Functions
1. **clean_string** or **cleanStr**
   - **Input parameter**:
     - `input_str` o `input` (string): Text string containing numbers and possible delimiters or special characters.
   - **Functionality**:
     Removes unwanted characters, such as delimiters, spaces, or special characters, leaving only the numbers to be processed later.
   - **Return value**:
     - `string`: Returns a clean string containing only the numbers and commas `,`.

2. **add**
   - **Input parameter**:
     - `numbers` or `inputStr` (string): Text string with numbers separated by delimiters.
   - **Functionality**:
     Converts the clean string of numbers into a list of integers and checks for the presence of negative numbers. If it finds a negative number, it throws an exception. (In **F#**, in case of an error, it returns `-1`). If there are no negative numbers, it performs the sum of the numbers.
   - **Return value**:
     - `int`: The total sum of the numbers present in the clean string.

## Installation

Clone this repository to your local machine:
   ```bash
   git clone git@github.com:Angiers18/enhanced_string_calculator_development.git
   ```
#### F#

Go to the project directory:
 ```bash
cd f#/StringCalculator
 ```

#### Python

Go to the project directory:
 ```bash
cd /python
 ```
## Use

#### F#

1. Call the `cleanStr` function to clean the string:

```f#
let cleanedString = cleanStr("//;\n1;2")  // "1,2"
 ```

2. Then, pass the cleaned string to the add function to get the sum:

```f#
let result = add cleanedString
 ```

3. Finally, print the result to the console:

```f#
printfn "The sum is: %d" result // Output: The sum is: 3
 ```

4. To run the program, use the command:

```bash
dotnet run
 ```

#### Python

1. Call the `clean_string` function to clean the string:

```python
cleanedString = clean_string("//;\n1;2") # "1,2"
 ```

2. Then, pass the cleaned string to the add function to get the sum:

```python
result = add(cleanedString)
 ```

3. Finally, print the result to the console:

```python
print(f"The sum is {result}") # Output: The sum is: 3
 ```

4. To run the program, use the command:

```bash
python main.py
 ```

## Tests

To run the tests for the string calculator, use the following command in Python:

```bash
python -m unittest test_string_calculator_artifact.py
 ```
