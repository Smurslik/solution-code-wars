#You are given an array (which will have a length of at least 3, but could be very large) containing integers.
#The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
#Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    count_even = 0
    for i in integers:
        if i % 2 == 0:
            count_even += 1
    if count_even > 1:
        for i in integers:
            if i % 2 == 1:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i     
