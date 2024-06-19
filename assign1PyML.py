'''#1
a=int(input("Enter a: "))
b=int(input("Enter b: "))
summation= a+b
print(f'Sum is equal to {summation}')

#2
def odd_even(c):
    if c%2 == 0:
        return "Even"
    else:
        return "Odd"
c=int(input("Enter number: "))
result=odd_even(c)
print(f'The number is {result}')

#3
def fact(d):
    if d == 0 or d == 1:
        return 1
    else:
        result = 1
        for i in range(2, d + 1):
            result *= i
        return result
d = int(input("Enter number: "))
result = fact(d)
print(f"The factorial is {result}.")

#4
name=str(input("Enter naame: "))
print(f'Welcome {name}!')

#5
def write_text(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
user_input = input("Enter a string to write to the file: ")
filename = "output.txt"
write_text(filename, user_input)
print(f"The string has been written to {filename}.")

#6
def read_and_print_file(output):
    try:
        with open(output, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {output} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
output = 'output.txt'  
read_and_print_file(output)

#7
str1=str(input("Enter a string: "))
print(len(str1))

#8
e=str(input("Enter first string: "))
f=str(input("ENter second string: "))
print(e+f)

#9
str3="Hello everybody! Welcom all!"
print(str3.find('people'))

#10
str4="Hello Sara"
print(str4.upper())

#11
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = int(input("Enter number: "))
print(fibonacci(n))

#12
def sum_of_digits(number):
    number = abs(number)
    digits = str(number)
    total = 0
    
    for digit in digits:
        total += int(digit)
    return total
number = int(input("Enter number: "))
print(f"The sum of the digits of {number} is {sum_of_digits(number)}.")

#13
birth=int(input("Enter birth year: "))
age = 2024-birth
if birth > 2024:
    print("Not possible.")
else:
    print(f'Your age is {age}.')

#14
def read_lines():
    lines = []
    while True:
        line = input("Enter a line: ")
        if line == "":
            break
        lines.append(line)
    print("\nGiven lines:")
    for line in lines:
        print(line)
read_lines()

#15
import csv
with open('data.csv', mode='r')as file:
    csvFile=csv.reader(file)
    for lines in csvFile:
        print(lines)

#16
def character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_string = str(input("Enter string: "))
frequency = character_frequency(input_string)
print("Character frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

#17
str10 = str(input("Enter string: "))
print(str10.title())

#18
def are_anagrams(str11, str12):
    str11 = str11.replace(" ", "").lower()
    str12 = str12.replace(" ", "").lower()
    return sorted(str11) == sorted(str12)
string11 = str(input("Enter string 1: "))
string12 = str(input("Enter string 2: "))
if are_anagrams(string11, string12):
    print("Given strings are anagrams.")
else:
    print("Given strings are not anagrams.")

#19
import string
def remove_punctuation(input_string):
    punctuation = string.punctuation
    result = input_string.translate(str.maketrans('', '', punctuation))
    return result
input_string = str(input("Enter string with punctuations: "))
print("String without punctuation:", remove_punctuation(input_string))

#20
def calculate_sum(numbers):
    total = sum(numbers)
    return total
number_list = [1, 2, 3, 4, 5, 6]
print("List of numbers:", number_list)
print("Sum of numbers:", calculate_sum(number_list))

#21
def count_occurrences(lst, element):
    count = lst.count(element)
    return count
my_list = [1, 2, 2, 3, 4, 2, 5]
print(my_list)
element_to_count = int(input("Enter number from list: "))
print(f"Number of occurrences of {element_to_count}: {count_occurrences(my_list, element_to_count)}")

#22
def min_max(n):
    if not n:
        return None, None
    return min(n), max(n)
n = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = min_max(n)
print(f"Minimum value: {min_value}")
print(f'Maximum value: {max_value}')

#23
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()
if unit == "C":
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is {converted_temp}°F")
elif unit == "F":
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is {converted_temp}°C")
else:
    print("Invalid unit")

#24
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = calculate(num1, num2, operator)
print(f"The result is: {result}")

#25
def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Contents of {source_file} have been copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file_contents(source_file, destination_file)

#26
def check_prefix_suffix(string, prefix=None, suffix=None):
    if prefix and string.startswith(prefix):
        print(f"The string starts with the prefix '{prefix}'.")
    elif prefix:
        print(f"The string does not start with the prefix '{prefix}'.")

    if suffix and string.endswith(suffix):
        print(f"The string ends with the suffix '{suffix}'.")
    elif suffix:
        print(f"The string does not end with the suffix '{suffix}'.")
string = input("Enter the string: ")
prefix = input("Enter the prefix to check (leave empty if not checking): ")
suffix = input("Enter the suffix to check (leave empty if not checking): ")
check_prefix_suffix(string, prefix, suffix)

#27
def string_to_char_list(string):
    return list(string)
string = input("Enter the string: ")
char_list = string_to_char_list(string)
print(f"The list of characters: {char_list}")'''        