class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        max_water_area = 0
        for _ in range(len(height) - 1):
            max_water_area = max((tail - head) * min(height[head], height[tail]), max_water_area)
            if head == tail:
                break
            if (height[head]) < (height[tail]):
                head += 1
            else:
                tail -= 1
        return max_water_area


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,2,4,3]))