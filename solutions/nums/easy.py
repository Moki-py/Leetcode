""" Easy problems for numbers """


class LengthOfLastWord:
    """ 9. Palindrome Number """
    def is_palindrome(self, x: int) -> bool:
        """Solution using string conversion"""
        return str(x) == str(x)[::-1]


class SolutionSearchInsertPosition:
    """ 35. Search Insert Position """
    def search_insert(self, nums: list[int], target: int) -> int:
        """ Binary search solution """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


class SolutionPlusOne(object):
    """ 66. Plus One """
    def plus_one(self, digits):
        """ Solution using string conversion """
        return [int(i) for i in str(int(''.join(map(str, digits))) + 1)]


class SolutionMySqrt(object):
    """ 69. Sqrt(x) """
    def my_sqrt(self, x):
        """ Solution using binary search """
        for i in range(0, int(x ** (0.5)) + 2):
            m = i*i
            if m > x:
                return i - 1
            elif m == x:
                return i


class SolutionClimbStairs(object):
    """ 70. Climbing Stairs """
    def climb_stairs(self, n):
        """ Solution using dynamic programming """
        if n == 1:
            return 1
        if n == 2:
            return 2

        osb = 2
        tsb = 1

        for _ in range(2, n):
            wtc = osb + tsb
            tsb = osb
            osb = wtc

        return wtc
