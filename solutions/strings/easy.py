class Solution:
    """ 58. Length of Last Word """
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[::-1][0])
