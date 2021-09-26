from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        d = {}
        for idx, num in enumerate(nums):
            d.setdefault(num, set()).add(idx)

        result = []
        size = len(nums)
        for idx in range(size - 3):
            num = nums[idx]
            if idx > 0 and num == nums[idx - 1]:
                continue

            for idx2 in range(idx + 1, size - 2):
                num2 = nums[idx2]
                if idx2 > idx + 1 and num2 == nums[idx2 - 1]:
                    continue

                for idx3 in range(idx2 + 1, size - 1):
                    num3 = nums[idx3]
                    num4 = target - (num + num2 + num3)
                    if num3 > num4:
                        break
                    elif idx3 > idx2 + 1 and num3 == nums[idx3 - 1]:
                        continue
                    idx_set = d.get(num4)
                    if idx_set and idx_set - set([idx, idx2, idx3]):
                        result.append([num, num2, num3, num4])
        return result