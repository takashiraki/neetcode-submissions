class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        i = 0

        for n in nums:
            ps = nums.copy()
            ps.pop(i)
            aa = 1
            for nn in ps:
                aa *= nn
                
            a.append(aa)
            i += 1
        return a