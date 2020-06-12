class Solution(object):
    def count_and_replace(self, s, return_int, target, number):
        return_int += s.count(target) * number
        s = s.replace(target, "0")
        return s, return_int
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return_int = 0
        special_value_dict = {
            "CM": 900, "CD": 400,
            "XC": 90, "XL": 40,
            "IX": 9, "IV": 4
        }
        value_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        for key, value in special_value_dict.items():
            s, return_int = self.count_and_replace(s, return_int, key, value)
        for key, value in value_dict.items():
            s, return_int = self.count_and_replace(s, return_int, key, value)
        return return_int


s = Solution()
print(s.romanToInt("IV"))