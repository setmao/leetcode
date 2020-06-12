class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_count = 0
        max_pos = 0
        extended_s = self.extend_s(s)
        for i in range(1, len(extended_s)):
            count = self.judge_palindrome(extended_s, i)
            if self.compare(extended_s, count, i, max_count, max_pos):
                max_count = count
                max_pos = i
        return extended_s[max_pos - max_count: max_pos + max_count + 1].replace(".", "")

    
    def extend_s(self, s):
        result = "."
        for char in s:
            result += char + "."
        return result

    def judge_palindrome(self, s, start):
        count = 0
        while ((start - count) >= 0) and ((start + count) < len(s)) and (s[start - count] == s[start + count]):
            count += 1
        return count - 1
    
    def compare(self, s, now_count, now_pos, max_count, max_pos):
        return (len(s[now_pos - now_count: now_pos + now_count + 1].replace(".", "")) >
                len(s[max_pos - max_count: max_pos + max_count + 1].replace(".", "")))



sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("ac"))