class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            
            l = n + 1
            r = len(nums) - 1

            while l < r:
                s = nums[n] + nums[l] + nums[r]

                if s == 0:
                    ans.append([nums[n],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[r + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return ans


