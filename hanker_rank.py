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