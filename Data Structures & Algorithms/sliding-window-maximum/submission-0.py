class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # https://docs.python.org/ja/3.14/library/collections.html
        dq = deque()
        res = []

        # デックにはインデックスを入れ
        # 対応する値が「常に単調現象」
        # になるように保つ
        for right in range(len(nums)):

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            

            left = right - k + 1
            
            if dq[0] < left:
                dq.popleft()

            if right >= k - 1:
                res.append(nums[dq[0]])

        return res