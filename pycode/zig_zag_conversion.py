class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        magic_num = (numRows * 2 - 2)
        if magic_num == 0:
            return s
        covert_matrix = [[0 for _ in range((len(s) // magic_num + 1) * (numRows - 1))] for _ in range(numRows)]
        for i in range(len(s)):
            round_num = i // magic_num
            case = i % magic_num
            if case < numRows:
                covert_matrix[case][round_num * (numRows - 1)] = s[i]
            else:
                covert_matrix[magic_num - case][round_num * (numRows - 1) + (case - numRows + 1)] = s[i]
        result = ""
        for row in covert_matrix:
            for ele in row:
                if ele != 0:
                    result += ele
        return result


    def convert_adv(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        magic_num = numRows * 2 - 2
        if magic_num == 0:
            return s
        # first line
        f = 0
        result = ""
        while f < len(s):
            result += s[f]
            f += magic_num
        # middle line
        for i in range(1, numRows - 1):
            j = i
            count = 0
            while j < len(s):
                result += s[j]
                if count == 0:
                    j += magic_num - 2 * i
                    count = 1
                else:
                    j += magic_num - (magic_num - 2 * i)
                    count = 0
        # last line
        l = numRows - 1
        while l < len(s):
            result += s[l]
            l += magic_num
        print(result)
        return result


sol = Solution()
sol.convert_adv("PAYPALISHIRING", 4)