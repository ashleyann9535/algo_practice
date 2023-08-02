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


#print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"

# Implement the function unique_in_order which takes as argument a sequence and 
# returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
def unique_in_order(sequence):
    if not sequence:
        return []

    new_arr = [sequence[0]]

    for item in sequence[1:]:
        if item != new_arr[-1]:
            new_arr.append(item)

    return new_arr

print(unique_in_order([1, 2, 2, 3, 3])) # [1, 2, 3]
print(unique_in_order('ABBCcAD')) # ['A', 'B', 'C', 'c', 'A', 'D']