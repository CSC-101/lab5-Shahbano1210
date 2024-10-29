import data


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3

def time_add(time1:data.Time, time2:data.Time)-> data.Time: # takes in two times and returns a new total time
    data.Time.newTime = (0,0,0)
    data.Time.newTime.hour = data.Time.time1.hour + data.Time.time2.hour
    data.Time.newTime.minute = data.Time.time2.minute + data.Time.time1.minute
    data.Time.newTime.second = data.Time.time1.seconds + data.Time.time2.seconds
    if data.Time.newTime.second > 59:
        data.Time.newTime.minute = data.Time.newTime.minute + 1
        data.Time.newTime.second = data.Time.newTime.second - 60
    return data.Time.newTime

# Part 4

def is_descending(list1:list[float]) -> bool: # takes in a list of float values and returns a bool depending
    # on if the list is descending
    Bool = []
    for i in list1:
        if list1[i] < list1[i+1]:
            Bool.append("True")
        else:
            Bool.append("False")
    if "False" not in Bool:
        return True
    else:
        return False


# Part 5

def largest_between(list1:list[int], lower:int, upper:int)-> int or None: # takes in a list of integers, and 2 integer
    # limits to return the index of the largest value
    largest = list1[0]
    largestIdx = 0
    if lower > upper or lower < 0 or upper < 0: # returns None if lower or upper are out of bounds
        return None
    for i in list1:
        if lower >= i and i >= upper:
            if list1[i] > largest:
                largest = list1[i]
                largestIdx = i
    return largestIdx

# Part 6

def furthest_from_origin(list1:list[data.Point])-> int or None: # takes in a list of points and returns the index of
    # the point that is the furthest from the origin
    distances = []
    dist = 0
    furthestIdx = 0
    if list1 == []:
        return None
    for i in list1:
        dist = ((i.x)**2 + (i.y)**2) **(1 / 2)
        distances.append(dist)
        print (dist)
    for j in range(len(distances)):
        print(j)
        if j < len(distances):
            if distances[j] > distances[j+1]:
                furthestIdx = j
    return furthestIdx