class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_value = 0
        
        for idx in range(len(s)):
            chars = set()
            
            for char in s[idx:]:
                if char in chars:
                    break
                else:
                    chars.add(char)
                    
            max_value = max([len(chars), max_value])
        return max_value
