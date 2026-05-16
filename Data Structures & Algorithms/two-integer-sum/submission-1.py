class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = 0 # 今いるところ
        for i in nums:

            n2 = n

            for l in nums[n + 1:]:
                n2+=1

                if i + l == target:
                    return [n,n2]

            n+=1