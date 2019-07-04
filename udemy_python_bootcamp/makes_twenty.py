'''
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
'''

def makes_twenty(n1,n2):
    return 20 in {n1,n2,n1+n2}

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

