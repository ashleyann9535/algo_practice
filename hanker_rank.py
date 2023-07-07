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


#WEEK TEST PREP Day 3
#Exercise 1
#Debug to get code working
#Given an array of  distinct integers, transform the array into a zig zag sequence by 
# permuting the array elements. A sequence will be called a zig zag sequence if the 
# first  k elements in the sequence are in increasing order and the last k  
# elements are in decreasing order, where k=(len(arr)+1)/2 . 
# You need to find the lexicographically smallest zig zag sequence of the given array.
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)//2) ## Was (n-1)/2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 ##Was n -1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 ##Was n+1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

#print(findZigZagSequence([1, 2, 3, 4, 5, 6, 7,], 7)) # 1 2 3 7 6 5 4

#Exercise 2
# Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally. 
# The rules of the game are as follows:
# Initially there are n towers.
# Each tower is of height  m.
# The players move in alternating turns.
# In each turn, a player can choose a tower of height x and reduce its height to y, 
# where 1<=y<x  and  evenly divides x.
# If the current player is unable to make a move, they lose the game.
# Given the values of n and m, determine which player will win. 
# If the first player wins, return 1 . Otherwise, return 2.

#Explanation: If there is one tower then Player 1 always wins by simply removing everything and 
# leaving just 1. But if there are two towers then second player can always just copy the 
# first player and therfore second player wins. If there are three towers then first one wins by 
# removing everything and leaving 1 and then just copying player two. 
# The only time that player one is going to lose if there is one tower which is it of height 1.
def towerBreakers(n, m):
    # Write your code here
    if m==1 or n%2 == 0:
        return 2
    else:
        return 1
    

#print(towerBreakers(2,6)) #2
#print(towerBreakers(1,4)) #2

#Exercise 3
#Complete the caesarCipher function in the editor below.
#caesarCipher has the following parameter(s):
# string s: cleartext and int k: the alphabet rotation factor
# Returns : string: the encrypted string
def caesarCipher(s, k):
    new_str = ''
    
    for i in range(len(s)):
        char = s[i]
        #In the context of the Caesar cipher implementation, ord() is used to get the ASCII code 
        # of a character before shifting it, while chr() is used to convert the shifted ASCII code 
        # back to a character after encryption
        if char.isupper():
            new_str += chr((ord(char)+ k - 65) % 26 + 65)
        elif char.islower():
            new_str += chr((ord(char) + k - 97) % 26 + 97)
        else:
            new_str += char
    
    return new_str

#print(caesarCipher('middle-Outz', 2)) #okffng-Qwvb

#Day 4 Exercise 1
#Given a square grid of characters in the range ascii[a-z], rearrange elements of each row 
# alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, 
# top to bottom. Return YES if they are or NO if they are not.
def gridChallenge(grid):
    rows_sorted = []
    for s in grid:
        sorted_str = ''.join(sorted(s))
        rows_sorted.append(sorted_str)
        
    print(rows_sorted)

    grouped_columns = [list(x) for x in zip(*rows_sorted)]
    print(grouped_columns)
    
    for l in grouped_columns:
     if l != sorted(l):
         return 'NO'
    
    return 'YES'

#Refactor to use list comp
# print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #YES

#Exercise 2
#Given an integer, we need to find the super digit of the integer.
#If x has only 1 digit, then its super digit is x.
#Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    else:
        current_sum = k * sum(int(digit) for digit in n)
        return superDigit(str(current_sum), 1)

print(superDigit('148', 3)) #3
print(superDigit('9875', 4)) #8