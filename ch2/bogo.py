from random import shuffle
import random

def bogoSort(a):
    n = len(a)
    i = 0
    while (is_sorted(a)== False):
        i += 1
        print(i)
        shuffle(a)
 
# To check if array is sorted or not
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True
 
# To generate permutation of the array
def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

a = [2,45,4,6,43,90,44,7,8,23,799]

bogoSort(a)