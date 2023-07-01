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

print(migratoryBirds([1, 4, 4, 4, 5, 3])) # 4
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])) #3

#WEEK TEST PREP Day 1
#Exercise 1
# Print the ratios of positive, negative and zero values in the array. 
# Each value should be printed on a separate line with  digits after the decimal. 
# The function should not return a value.
def plusMinus(arr):
    ratios = [0,0,0]
    for num in arr:
        if num == 0:
            ratios[2] += 1
        elif num < 0:
            ratios[1] += 1
        else:
            ratios[0] += 1
    
    for num in ratios:
        num = format((num/len(arr)),".6f")
        print(num)
        
    return ratios

#print(plusMinus([-4, 3, -9, 0, 4, 1]))

#Exercise 2
# Print two space-separated long integers denoting the respective minimum and maximum values 
# that can be calculated by summing exactly four of the five integers.
def miniMaxSum(arr):
    arr.sort()
    
    min_sum = arr[0] + arr[1] + arr[2] + arr[3]
    
    max_sum = arr[4] + arr[1] + arr[2] + arr[3]
    
    print(min_sum, max_sum)