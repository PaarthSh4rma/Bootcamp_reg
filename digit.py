'''
What the code does?
The code converts the given list to a number with the elements of the list as its digits.
'''

'''
How it is done?
The code reverses the given list and each element is multiplied by 10^(power). Power is initialised as 0.
Then this number is added to a variable 'number'.
This process is repeated for all elements in the reversed list with power incrementing by 1 afteer each iteration.
'''

given_list = [8,3,5,1,2,1]
given_list = given_list[::-1]  # reversing the list for esier working
power = 0  # power factor
number = 0  # Intialising the final number as 0 to start

for digit in given_list:
    number_add = digit * 10 ** power  # calculating place value of element
    power += 1  # incrementing power factor
    number += number_add  # adding element's place value to the final number

print(number)  # printing final number
