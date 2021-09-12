class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for idx, num in enumerate(nums[:-2]):
            idx2, idx3 = idx + 1, len(nums) - 1
            while idx2 < idx3:
                num2, num3 = nums[idx2], nums[idx3]
                total = num + num2 + num3
                if total == target:
                    return target
                elif total < target:
                    idx2 += 1
                else:
                    idx3 -= 1
                result = min(result, total, key=lambda x: abs(target - x))

        return result