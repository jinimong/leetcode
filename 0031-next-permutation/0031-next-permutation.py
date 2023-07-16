class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = self._find_desc_parts_prev_index(nums)
        
        if i == -1:
            # 없는 경우는 이미 최대 큰 수
            # 역정렬 처리
            nums.reverse()
            return
        
        # 찾은 수 보다 큰 수 중 최소값 찾기
        # (끝에서부터 비교하여 만나는 첫 큰 수)
        j = self._find_next_min_index(i, nums)

        # 찾은 두 수의 자리 변경
        nums[i], nums[j] = nums[j], nums[i]

        # 뒤의 자리수 역정렬
        nums[i+1:] = nums[i+1:][::-1]

    def _find_desc_parts_prev_index(self, nums: List[int]) -> int:
        # 끝에서부터 숫자가 작아지는 첫 인덱스 찾기
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                return i - 1
            i -= 1
        
        return -1

    def _find_next_min_index(self, i: int, nums: List[int]) -> int:
        # 비교 수 보다 큰 최소값 찾기
        # 내림차순 정렬된 배열이므로 뒤에서부터 비교 후 발견되면 즉시 리턴
        j = len(nums) - 1
        while j > i:
            if nums[i] < nums[j]:
                return j
            j -= 1
        
        return -1