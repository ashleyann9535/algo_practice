#The purpose of this function is to find the largest multiple of divisor 
#that is less than or equal to bound.
def max_multiple(divisor, bound):
    #First Attempt
    # for i in range(bound, 0, -1):
    #     if i % divisor == 0 and i > 0:
    #         return i

    #Refactor
    #Takes the Floor division then multiply it by the divisor
    return bound // divisor * divisor

# print(max_multiple(2,7)) #6
# print(max_multiple(10,50)) #50

#Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    #First Attempt
    # index = 0
    # phone = '('
    # for num in n:
    #     if index == 2:
    #         phone += str(num)
    #         phone += ') '
    #     elif index == 5:
    #         phone += str(num)
    #         phone += '-'
    #     else:
    #         phone += str(num)
    #     index += 1

    #Refactor
    # *n unpacks the items in each array
    phone = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

    return phone


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"