'''
SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 
every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 9, 6, 7, 8, 9, 11]) --> 14
'''

def summer_69(arr):
    index_6 = -1
    index_9 = -1
    for index,value in enumerate(arr):
        if value == 6:
            index_6 = index
        if value == 9:
            index_9 = index + 1
    arr = arr[:index_6] + arr[index_9:]
    if len(arr) == 0:
        return 0
    else:
        return(sum(arr))

print(summer_69([1,3,5]))
print(summer_69([6,7,8,9]))
print(summer_69([2,1,9,6,7,8,9,11]))


