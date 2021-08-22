class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p
        table = [[False] * len(p) for _ in range(len(s))]
        table[0][0] = True

        for pi in range(2, len(p)):
            if p[pi] == "*":
                table[0][pi] = table[0][pi - 2]

        for si in range(1, len(s)):
            for pi in range(1, len(p)):
                if p[pi] in {".", s[si]}:
                    table[si][pi] = table[si - 1][pi - 1]
                elif p[pi] == "*":
                    table[si][pi] = table[si][pi - 2] or (
                        table[si - 1][pi] and p[pi - 1] in {s[si], "."}
                    )

        return table[-1][-1]
