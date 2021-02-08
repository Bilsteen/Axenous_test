#Question 4:
#WAP which will input a positive integer n and output the number of divisors of n and sum of those divisors.
#(NOTE: Divisor means a positive integer from 1 to n).
#Test data : 42 , 147


from math import sqrt
def num_divisors(num):
    divisors = []
    for i in range(1,int(sqrt(num)+1)):
        if num%i == 0:
            if num/i != i:
                divisors.append(i)
                divisors.append(num/i)
            else:
                divisors.append(i)
    return divisors

divisors = num_divisors(42)
print(f"The divisors are {divisors}")
print(f"Sum of divisors is {sum(divisors)}")
divisors = num_divisors(147)
print(f"The divisors are {divisors}")
print(f"Sum of divisors is {sum(divisors)}")