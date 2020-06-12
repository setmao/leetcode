class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        appeared_char = []
        max_count = 0
        for char in s:
            if char not in appeared_char:
                appeared_char.append(char)
                if len(appeared_char) > max_count:
                    max_count = len(appeared_char)
            else:
                while appeared_char[0] != char:
                    appeared_char.pop(0)
                while char in appeared_char:
                    appeared_char.remove(char)
                appeared_char.append(char)
        return max_count


sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))
# print(sol.lengthOfLongestSubstring("bbbbb"))
# print(sol.lengthOfLongestSubstring("pwwkew"))
# print(sol.lengthOfLongestSubstring("dvdf"))
# print(sol.lengthOfLongestSubstring("ohvhjdml"))
print(sol.lengthOfLongestSubstring("aabaab!bb"))