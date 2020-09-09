# File Name: RoshanSreekanth_project.py
# Author Name: Roshan Sreekanth
# Description: Program to create a maths quiz for a teacher
import random

operator_string = "*/+-"
question_string = ""  # String accumulator that stores the questions.
answer_string = ""  # String accumulator that stores the questions along with the answers.

class_name = input("What is the class' name? ")
while class_name.isspace() or class_name == "":
    class_name = input("What is the class' name? ")

teacher_name = input("What is your name? ")
while teacher_name.isspace() or teacher_name == "":
    teacher_name = input("What is your name? ")

banner = "Class Name: " + class_name + "\nTeacher: " + teacher_name + "\n==============================\n"
# Banner to print the heading shown before the questions.

while True:  # If there is an error, the block of code restarts.
    try:
        max_questions = int(input("How many questions? "))
        while max_questions <= 0 or max_questions > 1000:  # Limits the questions to avoid negative or large numbers.
            max_questions = int(input("Wrong value! Please enter the number of questions:"))
        break
    except ValueError:  # In case an alphabet or a special character is entered instead of a number.
        print("Invalid input! Try again:")

while True:
    try:
        choice = int(input("1.Random\n2.Specific\n"))
        while choice != 1 and choice != 2:
            choice = int(input("Choose either 1 or 2 :"))
        break
    except ValueError:
        print("Wrong value! Try again")

if choice == 2:
    operator_choice = input("Choose your operator (*,/,+,-) ")
    while operator_choice not in operator_string or operator_choice == "":  # If the operators are not found in string
        operator_choice = input("Invalid operator! Try again: ")

for random_questions in range(max_questions):
    random_index = random.randint(0, 3)  # Specifies a random index to traverse the collection of operators.
    operator = operator_string[random_index]  # Traverses the operator string and assigns a random operator.

    if choice == 2:
        operator = operator_choice  # If a specific operator is chosen by the user, it is selected.

    right_num = random.randint(1, 12)
    left_num = random.randint(1, 12)  # Except for division, the left number is between 1 and 12.

    if operator == "/":
        operator = "\u00f7"  # Unicode for the division symbol
        left_num = random.randint(1, 144)  # For division, the limit is 144, as 12*12 is 144, ensuring the answer <= 12.
        while right_num > left_num:  # This loop ensures that the dividend > divisor. eg. 1/2 or 2/3 doesn't occur.
            right_num = random.randint(1, 12)
        while left_num // right_num > 12:  # This makes sure the quotient is <= 12.
            left_num = random.randint(1, 144)
            while left_num < right_num:  # To ensure dividend > divisor AND quotient <=12.
                left_num = random.randint(1, 144)

        answer = left_num // right_num

    if operator == "+":
        answer = left_num + right_num

    if operator == "-":
        while right_num > left_num:  # Prevents answers from being negative.
            right_num = random.randint(1, 12)
        answer = left_num - right_num

    if operator == "*":
        answer = left_num * right_num

    answer_string += str(random_questions+1) + ": " + str(left_num) + operator + str(right_num) + " = " + \
                         str(answer) + "\n"
    question_string += str(random_questions+1) + ": " + str(left_num) + operator + str(right_num) + " =\n"

try:  # In case of file errors, eg. disk too full, no permission etc.
    question_file = open(class_name + "_quiz.txt", "w")
    answer_file = open(class_name + "_answers.txt", "w")

    question_file.write(banner + question_string)
    answer_file.write(banner + answer_string)

    answer_file.close()
    question_file.close()
except IOError:
    print("File Error!")
