from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        start = 0
        end = len(height) - 1

        while (start < end):
            area = min(height[start], height[end]) * (end - start)
            result = max(area, result)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return result