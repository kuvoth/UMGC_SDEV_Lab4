"""

Devin Bulawa
SDEV 300 6381
6/5/2024

"""
import numpy as np


class InvalidInputException(Exception):
    """A user-defined exception class that validate the input entered"""


def mean(matrix):
    """determines the row and column mean values of the given matrix"""

    print("\nThe row and column mean values of the results are:")
    row = np.mean(matrix, axis=1)
    column = np.mean(matrix, axis=0)

    print("Row: ", end=" ")
    print(', '.join(str(f"{i:.2f}") for i in row))

    print("Column: ", end=" ")
    print(', '.join(str(f"{j:.2f}") for j in column))


def transpose(matrix):
    """provides the transpose of the given matrix"""

    print("\nThe transpose is:")

    mat_transpose = np.transpose(matrix)

    print_matrix(mat_transpose)


def element_mult(lst1, lst2):
    """multiplies each element of the first matrix by the second matrix"""

    print("\nYou selected Element by Element Multiplication. The results are:")

    result = np.multiply(lst1, lst2)

    print_matrix(result)
    transpose(result)
    mean(result)


def matrix_mult(lst1, lst2):
    """performs matrix multiplication on the two given matrices"""

    print("\nYou selected Matrix Multiplication. The results are:")

    result = np.matmul(lst1, lst2)

    print_matrix(result)
    transpose(result)
    mean(result)


def addition(lst1, lst2):
    """adds each element from the first matrix and the second matrix"""

    print("\nYou selected Addition. The results are:")

    result = np.add(lst1, lst2)

    print_matrix(result)
    transpose(result)
    mean(result)


def subtraction(lst1, lst2):
    """subtracts each element from the first matrix by the second matrix"""

    print("\nYou selected Subtraction. The results are:")

    result = np.subtract(lst1, lst2)

    print_matrix(result)
    transpose(result)
    mean(result)


def print_matrix(matrix):
    """prints matrix in 3x3 format"""

    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()


def valid_phone_num(phone_num):
    """Checks to see if a valid phone number was entered and
    raises an exception if not"""

    index = 0
    while True:
        try:
            if len(phone_num) != 12:
                raise InvalidInputException
            for i in phone_num:
                index += 1
                if index == 4 and i != '-':
                    raise InvalidInputException
                if index == 8 and i != '-':
                    raise InvalidInputException
                if index == (1, 2, 3, 5, 6, 7, 9, 10, 11, 12) \
                        and i is not i.isdigit():
                    raise InvalidInputException
            return False
        except InvalidInputException:
            phone_num = input("Invalid phone number entered. Please enter a phone number\n"
                              "in the format XXX-XXX-XXXX\n")


def valid_zipcode(zipcode):
    """checks to see if a valid zipcode was entered and
    raises an exception if not"""

    index = 0
    while True:
        try:
            if len(zipcode) != 10:
                raise InvalidInputException
            for i in zipcode:
                index += 1
                if index == 6 and i != "-":
                    raise InvalidInputException
                if not i.isdigit() and \
                        index == (1, 2, 3, 4, 5, 7, 8, 9, 10):
                    raise InvalidInputException
            return False
        except InvalidInputException:
            zipcode = input("Invalid zipcode entered. Please enter a zipcode\n"
                            "in the format XXXXX-XXXX\n")


def main():
    """main function used to run the python matrix application"""

    matrix1 = []
    matrix2 = []
    running = True

    print("***********Welcome to the Python Matrix Application"
          "***********")

    while running:
        print("\nDo you want to play the Matrix game?")

        while True:
            response = input("Enter Y for Yes or N for No:\n")
            try:
                if response.upper() != "Y" and response.upper() != "N":
                    raise InvalidInputException
                if response.upper() == "N":
                    print("***************************************************")
                    print("Thank you for trying the Python Matrix Application!")
                    print("***************************************************")
                    return False
                break
            except InvalidInputException:
                print("Invalid input detected.")

        phone_num = input("Enter your phone number (XXX-XXX-XXXX):\n")
        valid_phone_num(phone_num)

        zipcode = input("Enter your zipcode +4 (XXXXX-XXXX):\n")
        valid_zipcode(zipcode)

        while True:
            try:
                row1_a, row1_b, row1_c = input("Enter your first 3x3 matrix:\n").split()
                row2_a, row2_b, row2_c = input().split()
                row3_a, row3_b, row3_c = input().split()

                matrix1 = np.array([[row1_a, row1_b, row1_c], [row2_a, row2_b, row2_c],
                                    [row3_a, row3_b, row3_c]]).astype(int)
                break

            except ValueError:
                print("Invalid input detected. Please enter a matrix in the format\n"
                      "x x x\n"
                      "x x x\n"
                      "x x x")

        print("Your first matrix is:")
        print_matrix(matrix1)

        while True:
            try:
                row1_x, row1_y, row1_z = input("Enter your second 3x3 matrix:\n").split()
                row2_x, row2_y, row2_z = input().split()
                row3_x, row3_y, row3_z = input().split()

                matrix2 = np.array([[row1_x, row1_y, row1_z], [row2_x, row2_y, row2_z],
                                    [row3_x, row3_y, row3_z]]).astype(int)
                break

            except ValueError:
                print("Invalid input detected. Please enter a matrix in the format\n"
                      "x x x\n"
                      "x x x\n"
                      "x x x")

        print("Your second matrix is:")
        print_matrix(matrix2)
        while True:
            try:
                operation = input("Select a Matrix Operation from the list below:\n"
                                  "a. Addition\n"
                                  "b. Subtraction\n"
                                  "c. Matrix Multiplication\n"
                                  "d. Element by Element Multiplication\n")

                if operation.lower() == 'a':
                    addition(matrix1, matrix2)
                elif operation.lower() == 'b':
                    subtraction(matrix1, matrix2)
                elif operation.lower() == 'c':
                    matrix_mult(matrix1, matrix2)
                elif operation.lower() == 'd':
                    element_mult(matrix1, matrix2)
                else:
                    raise InvalidInputException
                break
            except InvalidInputException:
                print("Invalid input detected. \nPlease select"
                      " an option a-d")


main()
