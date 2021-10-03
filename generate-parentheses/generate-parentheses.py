class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {(0, 0): ["("]}
        vals = {"(": 1, ")": -1} # 괄호를 숫자에 매칭

        for i in range(n):
            for j in range(n):
                if (i, j) in dp:
                    continue
                prev_i = [
                    s + "("
                    for s in dp.get((i - 1, j), [])
                ]
                prev_j = [
                    s + ")"
                    for s in dp.get((i, j - 1), [])
                    if sum([vals[c] for c in s]) >= 1 # 숫자로 변환 후 총합계산
                ]
                dp[(i, j)] = prev_i + prev_j

        return [s + ")" for s in dp.get((n - 1, n - 1), [])]