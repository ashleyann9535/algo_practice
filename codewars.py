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

print(max_multiple(2,7)) #6
print(max_multiple(10,50)) #50