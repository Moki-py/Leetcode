""" Easy problems for numbers """


class LengthOfLastWord:
    """ 9. Palindrome Number """
    def is_palindrome(self, x: int) -> bool:
        """Solution using string conversion"""
        return str(x) == str(x)[::-1]
