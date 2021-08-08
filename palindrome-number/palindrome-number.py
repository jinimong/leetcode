class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        while s:
            if s[0] != s[-1]:
                return False
            s = s[1:-1]

        return True
