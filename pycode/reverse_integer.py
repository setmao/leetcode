class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)[::-1] if x >= 0 else str(x * -1)[::-1]
        reversed_x = int(str_x) if x >= 0 else int(str_x) * -1
        return reversed_x if pow(2, 31) * -1 <= reversed_x < pow(2, 31) else 0

sol = Solution()
sol.reverse(-11243123)
sol.reverse(1534236469)