'''
What it does?
The code converts the given list to a number with the elements of the list as its digits.
'''

'''
How it is done?
The code reverses the given list and each element is multiplied by 10^(power). Power is initialised as 0.
Then this number is added to a variable 'number'.
This process is repeated for all elements in the reversed list with power incrementing by 1 afteer each iteration.
'''

given_list = [8,3,5,1,2,1]
given_list = given_list[::-1]
power = 0
number = 0

for digit in given_list:
    number_add = digit * 10 ** power
    power += 1
    print(number_add)
    number += number_add

print(number)
