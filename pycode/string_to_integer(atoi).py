class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        return_data = ""
        no_whitespace_str = str.strip()
        if not no_whitespace_str:
            return 0
        elif no_whitespace_str[0] in "-1234567890":
            return_data += no_whitespace_str[0]
            for c in no_whitespace_str[1:]:
                if c.isdigit():
                    return_data += c
                else:
                    break
            if return_data in "+-":
                return 0
            # for overflow
            if abs(int(return_data)) > (2 ** 31 - 1):
                if int(return_data) < 0:
                    return (2 ** 31) * -1
                else:
                    return (2 ** 31 - 1)
            return int(return_data)
        else:
            return 0


s = Solution()
print(s.myAtoi("   -43"))