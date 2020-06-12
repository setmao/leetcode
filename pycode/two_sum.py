class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked_nums = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in checked_nums:
                return [checked_nums[ans], i]
            else:
                checked_nums[nums[i]] = i

    def two_sum_list(self, nums, target):
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in nums[i + 1:]:
                return [i, nums.index(ans) + i + 1]

sol = Solution()
print(sol.two_sum([3, 3], 6))
print(sol.two_sum_list([3, 3], 6))