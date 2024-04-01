""" Easy string problems solutions """


class SolutionLengthOfLastWord:
    """ 58. Length of Last Word """
    def length_of_last_word(self, s: str) -> int:
        """Solution using string conversion"""
        w = s.split()
        return len(w[::-1][0])


class SolutionRomanToInt:
    """ 13. Roman to Integer """
    def roman_to_int(self, s: str) -> int:
        """Solution using dictionary"""
        rom_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            }
        result = 0

        for n, char in enumerate(s):
            if n < len(s) - 1 and rom_nums[char] < rom_nums[s[n+1]]:
                result -= rom_nums[char]
            else:
                result += rom_nums[char]

        return result
