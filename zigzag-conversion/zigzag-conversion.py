class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if len(s) == numRows:
            return s
            
        result = ["" for _ in range(numRows)]
        row = 0
        for idx, char in enumerate(s):
            # 해당하는 행에 글자 더해주기
            result[row] += char
            # 방향이 바뀌는 기준으로 열 번호를 매기기
            col = idx // (numRows - 1)
            # 열 번호가 짝수면 아래로, 홀수면 위로 방향 변경
            sign = 1 if col % 2 == 0 else -1
            row += sign
            
        return "".join(result)