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

# print(unique_in_order([1, 2, 2, 3, 3])) # [1, 2, 3]
# print(unique_in_order('ABBCcAD')) # ['A', 'B', 'C', 'c', 'A', 'D']

# An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, 
# then the remaining numbers were mixed. Find the number that was deleted.
#If no number was deleted from the starting array, your function should return the int 0.
def find_deleted_number(arr, mixed_arr):
    #First Attempt
    # if len(arr) == len(mixed_arr):
    #     return 0

    # arr = set(arr)
    # mixed_arr = set(mixed_arr)

    # missing_num = list(arr - mixed_arr)

    # return missing_num[0]

    #Refactor way
    return sum(arr) - sum(mixed_arr)

#print(find_deleted_number([1,2,3,4,5,6,7,8,9],[3,2,4,6,7,8,1,9]))

#Given two array of integers(arr1,arr2). Your task is going to find a pair of numbers
# (an element in arr1, and another element in arr2), their difference is as big as possible(absolute value); 
# Again, you should to find a pair of numbers, their difference is as small as possible. 
# Return the maximum and minimum difference values by an array: [  max difference,  min difference  ]
#attempt 1
# def max_and_min(arr1,arr2):
#     max_min_arr = []

#     max_val_arr1 = max(arr1)
#     min_val_arr2 = min(arr2)
    
#     max_val_arr2 = max(arr2)
#     min_val_arr1 = min(arr1)

#     diff1 = abs(max_val_arr1 - min_val_arr2)
#     diff2 = abs(min_val_arr1 - max_val_arr2)

#     if diff1 > diff2:
#         max_min_arr.append(diff1)
#     else:
#         max_min_arr.append(diff2)

#     arr1.sort()
#     arr2.sort()
#     min_diff = float('inf')  # Initialize with positive infinity
    
#     i = 0
#     for n in arr2:
#         while i < len(arr1) - 1 and abs(arr1[i+1] - n) < abs(arr1[i] - n):
#             i += 1
#         min_diff = min(min_diff, abs(arr1[i] - n))

#     max_min_arr.append(min_diff)

#     return max_min_arr

#attempt 2 with list comp
def max_and_min(arr1, arr2):
    max_min = [abs(y-x) for x in arr1 for y in arr2]
    print(max_min)

    return [max(max_min), min(max_min)]


print(max_and_min([3,10,5],[20,7,15,8])) # 17, 2
print(max_and_min([3],[20])) # 17, 17