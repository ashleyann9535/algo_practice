# Given an array of bird sightings where every element represents a bird type id, determine 
#the id of the most frequently sighted type. If more than 1 type has been spotted that maximum 
#amount, return the smallest of their ids.
# Example
# There are two each of types  and , and one sighting of type .
# Pick the lower of the two types seen twice: type 

def migratoryBirds(arr):
    arr.sort()

    most_bird = max(set(arr), key = arr.count)
    
    return most_bird

#print(migratoryBirds([1, 4, 4, 4, 5, 3])) # 4
#print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])) #3

#A person wants to determine the most expensive computer keyboard and USB drive 
#that can be purchased with a give budget. 
#Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
#If it is not possible to buy both items, return -1.
def getMoneySpent(keyboards, drives, b):
    prices_under_budget = []

    for k in keyboards:
        for d in drives:
            spent = k + d
            if spent <= b:
                prices_under_budget.append(spent)

    if len(prices_under_budget) > 0:
        return max(prices_under_budget)
    else: 
        return -1

# print(getMoneySpent([40, 50, 60], [5,8,12], 60)) #58
# print(getMoneySpent([3,1], [5,2,8], 10)) #9
# print(getMoneySpent([4], [5], 5)) #-1

#The Utopian Tree goes through 2 cycles of growth every year. Each spring, 
# it doubles in height. Each summer, its height increases by 1 meter.
#A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. 
# How tall will the tree be after n growth cycles?
def utopianTree(n):
    tree = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            tree += 1
        else:
            tree *= 2
    
    return tree

#print(utopianTree(5)) #14

#An integer d is a divisor of an integer n if the remainder of n/d=0.
#Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
# Count the number of divisors occurring within the integer.
def findDigits(n):
    num_to_str = str(n)
    count = 0
    
    for char in num_to_str:
        num = int(char)
        if num != 0 and n % num == 0:
            count += 1
            
    return count

#print(findDigits(124)) #3

#Given a range of numbered days, [i...j] and a number k, determine the number of days in the range 
# that are beautiful. Beautiful numbers are defined as numbers where i - reverse(i) is evenly 
# divisible by k. If a day's value is a beautiful number, it is a beautiful day. 
# Return the number of beautiful days in the range.
def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for n in range(i,j+1):
        reverse_n = str(n)[::-1]
        abs_diff = abs(n - int(reverse_n))
        if abs_diff % k == 0:
            count += 1
            
    return count


#print(beautifulDays(20, 23, 6)) #2

# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a 
# number line ready to jump in the positive direction (i.e, toward positive infinity).
# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as 
# part of the show. If it is possible, return YES, otherwise return NO.
def kangaroo(x1, v1, x2, v2):
    # If the kangaroos start at the same location and have the same speed, they will always meet.
    if x1 == x2 and v1 == v2:
        print(1)
        return "YES"
    
    # If the kangaroos start at different locations and have the same speed, they will never meet.
    if v1 == v2 and x1 != x2:
        print(2)
        return "NO"
    
    # Calculate the time it takes for the kangaroos to meet.
    # The condition for meeting is (x1 + t * v1) == (x2 + t * v2).
    t = (x2 - x1) / (v1 - v2)

    # If t is a positive integer, it means the kangaroos meet at the same location at the same time.
    if t >= 0 and t.is_integer():
        print(4)
        return 'YES'
    else:
        print(5)
        return 'NO'

# print(kangaroo(0, 3, 4, 2)) #yes
# print(kangaroo(0, 2, 5, 3)) #no
# print(kangaroo(2, 1, 1, 2)) #yes
# print(kangaroo(28, 8, 96, 2)) #no

def extraLongFactorials(n):
    # Write your code here
    factorials = 1

    for i in range(1, n + 1):
        factorials *= i
        
    return factorials

print(extraLongFactorials(25))