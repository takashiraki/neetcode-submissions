class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        
        a = 0

        while l < r:
            mh = min(heights[l],heights[r])
            w = r - l

            a = max(a, mh * w)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return a