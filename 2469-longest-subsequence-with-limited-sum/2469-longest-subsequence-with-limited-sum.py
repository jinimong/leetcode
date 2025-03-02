class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix_sum = [0]
        for i, num in enumerate(sorted(nums), start=1):
            prefix_sum.append(prefix_sum[i - 1] + num)
        
        # sorted array = [1,2,4,5]
        # prefix_sum = [0,1,3,7,12]

        return [
            bisect.bisect_right(prefix_sum, query) - 1
            for query in queries
        ]         
        