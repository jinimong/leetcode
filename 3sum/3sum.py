from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        sorted_keys = sorted(counter.keys())
        result = []

        for idx, num in enumerate(sorted_keys):
            target = -1 * num
            for num2 in sorted_keys[idx:]:
                num3 = target - num2
                if num3 < num2:
                    break
                if not num3 in counter:
                    continue

                used_counter = Counter([num, num2, num3])
                is_over_cnt = False
                for used_num, cnt in used_counter.items():
                    if counter[used_num] < cnt:
                        is_over_cnt = True
                        break
                if is_over_cnt:
                    continue

                result.append([num, num2, num3])

        return result