# 1 Remove all whitespace from object (string)
def no_space(x):
    return x.replace(" ", "")

# 2 Multiply two integers and return the product
def multiply(a, b):
  return a * b

# 3 Return (Even) or (Odd) depending on the integer value of (number)
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# ALTERNATE SOLUTIONS
def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'

# 4 Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
def find_short(s):
      a = min(s.split(' '), key=len)
      return len(a)
# ALTERNATE SOLUTIONS
def find_short(s):
    return min(len(x) for x in s.split())

def find_short(s):
    s = s.split()
    return len(min(s, key = len))

# 5 Sum all the numbers of the array (in F# and Haskell you get a list)
# except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge,
# even if there are more than one with the same value!)
def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# 6 In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
def high_and_low(numbers):
    nums = map(int, numbers.split(" "))
    return " " .join(map(str, (max(nums), min(nums))))

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

# 7 Find the average of a list (array), if the list is empty, still return 0.
def find_average(array):
    if len(array) == 0:
        return 0
    else:
        return sum(array)/len(array)

# 8 Return the given string (st) with the order of words reversed.
def reverse(st):
    return " ".join(st.split()[::-1])

# 9 Given n (number of times someone hoola-hoops),
# if (n) is greater than or equal to 10 (see if statement), else (see else statement)
def hoopCount(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"

def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"

# 10 (Took a long time to figure out the import groupby tool, and itertools)
# sum(l) and len(l), these are getting easy to remember
# Extract integers from string, sum the list of extracted integers.
def sum_from_string(string):
    from itertools import groupby
    l = [int(''.join(i)) for is_digit, i in groupby(string, str.isdigit) if is_digit]
    return sum(l)

import re
def sum_from_string(string):
    d = re.findall("\d+",string)
    return sum(int(i) for i in d)

# 11 Return boolean (true, false) confirming if (string) is an isogram (contains no duplicate characters).
def is_isogram(string):
    line = string.upper()
    if not line:
        return True
    for x in line:
        if line.count(x) > 1:
            return False
    return True

def is_isogram(string):
    return len(string) == len(set(string.lower()))

#  12 Simple correction of 'order of operations' function.
def calculate(a, b, c):
    return (a + b) * c

# 13 Return true if string contains only digits, false otherwise or false if empty.
def is_digit(n):
    return n.isdigit() and len(n)==1

# 14 Find length of shortest word in string. (Python sort is alphabetic. you have to define key=len)
def find_short(s):
    list = s.split()
    return len(sorted(list, key=len)[0])

def find_short(s):
    return min(len(x) for x in s.split())

# 15 Your friend advised you to see a new performance in the most popular theater in the city.
# He knows a lot about art and his advice is usually good, but not this time:
# the performance turned out to be awfully dull. It's so bad you want to sneak out,
# which is quite simple, especially since the exit is located right behind your row to the left.

# All you need to do is climb over your seat and make your way to the exit.
# The main problem is your shyness: you're afraid that you'll end up blocking the view
# (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns
# to your left. To gain some courage, you decide to calculate the number of such people and see if you can
# possibly make it to the exit without disturbing too many people.

# Given the total number of rows and columns in the theater (nRows and nCols, respectively),
# and the row and column you're sitting in, return the number of people who sit strictly
# behind you and in your column or to the left, assuming all seats are occupied.
def seats_in_theater(tot_cols, tot_rows, col, row):
    above = tot_cols - (col - 1)
    to_left = tot_rows - (row)
    behind = above * to_left
    return behind

#  16 Create a method is_uppercase() to see whether the string is ALL CAPS.
def is_uppercase(inp):
    return inp.isupper()

#  17 Give a list, find the average of all the values.
def get_average(marks):
    return sum(marks) / len(marks)

#  18 Write a function getMean that takes as parameters an array (arr) and 2 integers (x and y).
#  The function should return the mean between the mean of the the first x elements of the array and
#  the mean of the last y elements of the array.
#  The mean should be computed if both x and y have values higher than 1 but less or equal to the array's length.
#  Otherwise the function should return -1.
def get_mean(arr,x,y):
    if x == 1 or y == 1 or x > len(arr) or y > len(arr):
        return -1
    mean_x = sum(arr[:x])/len(arr[:x])
    mean_y = sum(arr[-y:])/len(arr[-y:])
    return (mean_x + mean_y) / 2

# 19 Consider an array of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
# (The array is long, and entirely filled with True, False)
def count_sheeps(array1):
    count = 0
    for x in array1:
        if x == True:
            count +=1
    return count

#  20 One flowers petals are even and one flowers petals are odd == true, else false.
def lovefunc( flower1, flower2 ):
   return False if (flower1 + flower2) % 2 == 0 else True
# BETTER
 def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

#  21 YEESS! Write a function numberJoy() which tests if a positive integer n is Harshad,
# and returns True if the product of its digit sum, and its digit sum reversed, equals n. Otherwise return False.
def numberJoy(n):
    listed = map(int, str(n))
    digit_sum = sum(listed)
    rev_digit_sum = int(str(digit_sum)[::-1])
    return True if digit_sum * rev_digit_sum == n else False

#  22 Given a list (numbers),
#  square each object (integer) in the list and then return the sum of all squared objects.
def square_sum(numbers):
    sq = [x ** 2 for x in numbers]
    return sum(sq)

#  23 Given a list of integers, invert the values of all integers from negative to positive or positive to negative.
def invert(lst):
    return [-x for x in lst]

#  24 Compare two lists and return boolean based on whether they contain any of the same values.
def duplicate_elements(m, n):
    return bool(set(m) & set(n))

#  25 "Volume of a Cuboid" - Return the volume of a cube, given the dimensions.
def getVolumeOfCubiod(length, width, height):
    return length * width * height

#  26 (super simple) "Convert a Number to a String!" - Return integer give a number value as string.
def number_to_string(num):
    return str(num)

#  27 "Plural" - We need a simple function that determines if a plural is needed or not. 
#     It should take a number, and return true if a plural should be used with that number or false if not.
#     This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
def plural(n):
    return False if n == 1 else True
