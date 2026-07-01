class Solution:
    def trap(self, height: List[int]) -> int:
        a = 0

        lm = [0] * len(height)
        rm = [0] * len(height)

        for i in range(1, len(height)):
            lm[i] = max(lm[i-1], height[i-1])

        for ir in range(len(height) - 2, -1, -1):
            rm[ir] = max(rm[ir + 1], height[ir + 1])

        for ar in range(len(height)):
            ta = min(lm[ar],rm[ar]) - height[ar]

            if ta > 0:
                a += ta
        return a