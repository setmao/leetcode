class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        legal_str = "1234567890-+"
        result_str = ""
        neg = 0
        for char in str.replace(" ",""):
            if char not in legal_str:
                break
            result_str += char
        if not result_str or result_str == "-" or result_str == "+":
            return 0
        if result_str[0] == "-":
            neg = 1
        result_str = result_str.replace("-", "")
        result = int(result_str)
        if neg:
            result *= -1
            if result <= pow(2, 31) * -1:
                return pow(2, 31) * -1
        return result if result < pow(2, 31) else pow(2, 31)


sol = Solution()
print(sol.myAtoi("words and 987"))
print(sol.myAtoi("-91283472332"))
print(sol.myAtoi("   -42"))
print(sol.myAtoi("   -42-"))
print(sol.myAtoi("4193 with words"))