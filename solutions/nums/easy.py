class Solution:
    """ 9. Palindrome Number """
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]