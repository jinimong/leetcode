class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend * divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        for shift in range(31, -1, -1):
            target = dividend >> shift
            Q = target - divisor
            result <<= 1
            if Q >= 0:
                result += 1
                tail_diviend = ((2 ** shift) - 1) & dividend
                dividend = (Q << shift) | tail_diviend

        result *= sign
        min_range, max_range = -(2 ** 31), 2 ** 31 - 1
        
        if result < min_range:
            return min_range
        elif result > max_range:
            return max_range
        return result