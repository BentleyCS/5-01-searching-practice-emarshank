import random
def randomSearch(items:list, target) -> int:
    tries = 0
    while True:
        tries += 1
        randomnum = random.randint(0, len(items)-1)
        if items[randomnum] == target:
            break
    print(tries)
    return randomnum
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value

def linearSearch(items:list, target) -> tuple[int,int]:
    tries = 0
    for index in range(0, len(items)):
        tries += 1
        if items[index] == target:
            return index, tries
    return -1, tries
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.

def binarySearch(items:list, target) -> tuple[int,int]:
    low = 0
    high = len(items)-1
    checks = 0
    while high >= low:
        mid = int((low + high) / 2)
        checks += 1
        if items[mid] == target:
            return mid, checks
        if items[mid] > target:
            high = mid-1
        if items[mid] < target:
            low = mid+1
    return -1, checks

    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
print(binarySearch([1,3,5,7,9],7))