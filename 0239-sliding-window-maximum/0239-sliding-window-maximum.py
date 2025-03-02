class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_val = None
        window = collections.deque()
        result = []

        for i, num in enumerate(nums):
            # 현재 윈도우를 벗어난 인덱스 제거
            while window and window[0] < i - k + 1:
                window.popleft()
                
            # 새로운 값보다 작은 기존 값들은 모두 제거 (최대값 후보가 될 수 없음)
            while window and nums[window[-1]] < num:
                window.pop()
                
            # 현재 인덱스 추가
            window.append(i)
            
            # 첫 윈도우 완성 후부터 결과 추가
            if i >= k - 1:
                max_idx = window[0]  # window[0]는 항상 현재 윈도우의 최대값 인덱스
                result.append(nums[max_idx])
                
        return result
