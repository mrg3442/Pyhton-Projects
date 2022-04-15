#
# Python: 3.10.0
#
# Author: Matthew Green
#
# Purpose: The Tech Academy - Python Course, creating our first program together
#           Demonstrating how to pass variables from function to function
#           while producing a functional game
#
#
#           Remember, function_name(variable) _means that we pass in the var
#           return variable _means that we are returning the variable
#           back to the calling function.


def start():
    f_name = 'Sarah'
    l_name = 'Conner'
    age = 28
    gender = 'Female'
    get_name(f_name, l_name, age, gender)


def get_name(f_name, l_name, age, gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name, l_name, age, gender))





if __name__ == '__main__':
    start()
