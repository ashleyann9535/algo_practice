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

#miniMaxSum([1, 2, 3, 4, 5]) #10 14

def timeConversion(s):
    # Write your code here
    if s[-2:] == 'PM' and s[:2] != '12':
        hour = int(s[:2]) + 12
        #print(s[:2])
        # print(s[2:8])
        time = str(hour)+ s[2:8]
    elif s[-2:] == 'AM' and s[:2] == '12':
        hour = '00'
        time = hour+ s[2:8]
    else:
        time = s[:-2]
    return time

# print(timeConversion('07:05:45PM')) # 19:05:45
# print(timeConversion('12:05:45AM')) # 00:05:45
# print(timeConversion('12:05:45PM')) # 12:05:45

#WEEK TEST PREP Day 2
#Exercise 1
#Given an array of integers, where all elements but one occur twice, find the unique element.
#Return the element that occurs only once
def lonely_integer(a):
    a.sort()
    for num in a:
        if a.count(num) == 1:
            unique = num
    return unique

#print(lonely_integer([1,2,3,4,3,2,1])) #4

#Exercise 2
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(arr, n):
    #Use if always a 3 by 3 square
    #left = arr[0][0] + arr[1][1] + arr[2][2]
    #right = = arr[0][2] + arr[1][1] + arr[2][0]
    left = 0
    right = 0
    for i in range(n):
        left += arr[i][i]

    for i in range(n):
        right += arr[i][n-i-1]

    return abs(left - right)

matrix = [[11, 2, 4],
          [4, 5, 6],
          [10, 8, -12]]

#print(diagonalDifference(matrix, 3)) #15

#Exercise 3
#Given a list of integers, count and return the number of times each value appears 
# as an array of integers. Note: always return a frequency array with 100 elements, if want just number
# in array is max()+1
def countingSort(arr):
    # Write your code here
    freq_arr = [0]*100
    
    for num in arr:
        freq_arr[num] += 1
    
    return freq_arr

#print(countingSort([1,1,3,2,1])) #[0,3,1,1]
#print(countingSort([63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]))