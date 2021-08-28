class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        i = 0
        while i < len(shortest):
            if len(set(map(lambda s: s[i], strs))) != 1:
                break
            i += 1

        return shortest[:i]