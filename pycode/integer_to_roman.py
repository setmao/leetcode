class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return_str = ""

        M_cnt = num // 1000
        num -= M_cnt * 1000
        return_str += "M" * M_cnt

        if num // 100 == 9:
            return_str += "CM"
            num -= 900
        elif num // 100 == 4:
            return_str += "CD"
            num -= 400
        else:
            D_cnt = num // 500
            num -= D_cnt * 500
            return_str += "D" * D_cnt
            C_cnt = num // 100
            num -= C_cnt * 100
            return_str += "C" * C_cnt

        if num // 10 == 9:
            return_str += "XC"
            num -= 90
        elif num // 10 == 4:
            return_str += "XL"
            num -= 40
        else:
            L_cnt = num // 50
            num -= L_cnt * 50
            return_str += "L" * L_cnt
            X_cnt = num // 10
            num -= X_cnt * 10
            return_str += "X" * X_cnt

        if num == 9:
            return_str += "IX"
            return return_str
        elif num == 4:
            return_str += "IV"
            return return_str
        else:
            V_cnt = num // 5
            num -= V_cnt * 5
            return_str += "V" * V_cnt
            I_cnt = num
            return_str += "I" * I_cnt
            return return_str


s = Solution()
print(s.intToRoman(1994))