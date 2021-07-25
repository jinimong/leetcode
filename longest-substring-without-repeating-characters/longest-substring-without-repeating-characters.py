class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_value = 0
        start_idx = 0
        
        for idx, char in enumerate(s):
            idx2 = d.get(char)
            if idx2 is not None and start_idx <= idx2:
                start_idx = idx2 + 1
            else:
                max_value = max(max_value, idx - start_idx + 1)
            d[char] = idx
            
        return max_value
