class Solution:
    def trap(self, height: List[int]) -> int:
        a = 0
        for n in range(len(height)):
            if n == 0 or n == len(height) - 1:
                continue


            ta = min(max(height[:n]),max(height[n + 1:])) - height[n]
            if ta < 0:
                continue
            a += ta
        return a

            