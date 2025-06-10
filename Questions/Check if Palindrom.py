class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        result = 0
        while x > 0:
            ld = x %10
            result = (result*10) + ld
            x = x//10
        return result ==  x

Solution().isPalindrome(121)


# opimised solution


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  # Negative numbers are not palindromes
        s = str(x)
        rev = s[::-1]
        return s == rev   # Or: return x == int(rev)

        