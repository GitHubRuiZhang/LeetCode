# python3
# We define the Perfect Number is a positive integer that is equal to
# the sum of all its positive divisors except itself.

# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)


# My solution
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum_pn = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_pn += i
                sum_pn += (num / i)

        return sum_pn == num


# My solution II
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        prime_numbers = [2,3,5,7,13,17,19,31]
        i = 0
        while 2**(prime_numbers[i]-1) * (2**prime_numbers[i] - 1) < num:
            i += 1
        return 2**(prime_numbers[i]-1) * (2**prime_numbers[i] - 1) == num