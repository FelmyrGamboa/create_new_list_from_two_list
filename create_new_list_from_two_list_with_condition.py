# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain 
# odd numbers from the first list and even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:

# result list: [25, 35, 40, 60, 90]


#Create a function that would check the list of odd numbers
def check_numbers_if_odd(number_list):
#Create a for loop with a condition if the number is odd
    for numbers in number_list:
        if numbers % 2 != 0:
            result_list.append(numbers)

#Create a function that would check the list of even numbers
def check_numbers_if_even(number_list):
#Create a for loop with a condition if the number is even
    for numbers in number_list:
        if numbers % 2 == 0:
            result_list.append(numbers)

#Create a list that would store the results of the functions
result_list = list()

#Create the list of given numbers
number_list_1 = [10, 20, 25, 30, 35]
number_list_2 = [40, 45, 60, 75, 90]

#Call out the function 
check_numbers_if_odd(number_list_1)
check_numbers_if_even(number_list_2)

#Display the result
print("Result list: ", result_list)