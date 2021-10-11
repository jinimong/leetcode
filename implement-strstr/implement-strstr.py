class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        
        if n > h:
            return -1
        elif n == h and needle == haystack:
            return 0
        
        for i in range(h - n + 1):
            if haystack[i : i + n] == needle:
                return i
            
        return -1
            