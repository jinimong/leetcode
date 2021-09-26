class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        opens = set(pairs.keys())

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if pairs[stack[-1]] != c:
                    return False
                stack.pop()

        return len(stack) == 0