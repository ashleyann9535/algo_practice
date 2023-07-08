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


print(getMoneySpent([40, 50, 60], [5,8,12], 60)) #58
print(getMoneySpent([3,1], [5,2,8], 10)) #9
print(getMoneySpent([4], [5], 5)) #-1