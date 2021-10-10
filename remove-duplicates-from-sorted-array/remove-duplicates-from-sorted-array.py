class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev_num = None
        
        while i < len(nums):
            if prev_num == nums[i]:
                nums.pop(i)
            else:
                prev_num = nums[i]
                i += 1
        
        return i