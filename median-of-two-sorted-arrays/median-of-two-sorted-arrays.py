class Solution:
    def merge_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        while True:
            if len(nums1) == 0:
                result += nums2
                break
            elif len(nums2) == 0:
                result += nums1
                break
            
            if nums1[0] < nums2[0]:
                result.append(nums1.pop(0))
            else:
                result.append(nums2.pop(0))
                
        return result
    
    def median(self, nums: List[int]) -> float:
        length = len(nums)
        center = length // 2
        if length % 2 == 0:
            return (nums[center - 1] + nums[center]) / 2
        return nums[center] / 1

        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = self.merge_sort(nums1, nums2)
        return self.median(sorted_nums)
            