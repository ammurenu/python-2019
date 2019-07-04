'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
'''

def count_primes(num):
    count = 0
    for i in range(2,num+1):
        for y in range(2,i):
            if i % y == 0:
                break
        else:
            count += 1
    return count

print(count_primes(100))
print(count_primes(25))


