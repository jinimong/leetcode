class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for idx in range(len(s)):
            odd = self.palindrome(idx, idx, s)
            even = self.palindrome(idx, idx + 1, s)
            result = max(odd, even, result, key=len)
        return result

    def palindrome(self, left: int, right: int, s: str) -> str:
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
    