import math
# Math is imported to get the next lowest integer from a decimal number.
# for example ceil(3.5) = 4, ceil(3.1)= 4, ceil(3.9)=4


def sigma2(n):
    '''
    This function is used to calculate the square of the divisors.
    Here, first the divisors are obtained and then they are squared and summed
    '''
    divisors = set()
    for i in range(1, math.ceil(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
    divisors.add(n)
    squared_divisors = [i*i for i in divisors]
    return sum(squared_divisors)


def SIGMA2(n):
    '''
    This function is used to calculate the summatory function od sigma2.
    each number in the range from 1 to that numbers sigma2 value is calculated and summed
    '''
    total = 0
    for i in range(1, n+1):
        total += sigma2(i)
    return total


# for i in range(1, 7):
#     print(i, SIGMA2(i))
# Uncomment the above 2 lines of code for testing whether
# the answer is correct for test cases given in the question

# Final output
print(SIGMA2(1015) % 109)
