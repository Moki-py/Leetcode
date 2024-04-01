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


class SolutionLongestCommonPrefix:
    """14. Longest Common Prefix"""
    def longest_common_prefix(self, strs: list[str]) -> str:
        """Solution using string slicing"""
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


class SolutionAddBinary:
    """ 67. Add Binary """
    def add_binary(self, a: str, b: str) -> str:
        """ Solution using binary conversion """
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)

        decimal_sum = decimal_a + decimal_b

        binary_sum = bin(decimal_sum)[2:]

        return binary_sum


class SolutionConvertToTitle:
    """ 168. Excel Sheet Column Title """
    def convert_to_title(self, column_number: int) -> str:
        """ Solution using string conversion """
        title = ""
        while column_number > 0:
            column_number -= 1
            title = chr(column_number % 26 + ord('A')) + title
            column_number //= 26
        return title
