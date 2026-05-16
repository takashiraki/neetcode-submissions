class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        n = 0
        for i in nums:

            ans = target - i

            # 自分以降のリスト内にあった場合
            if ans in s:
                return [s.get(ans),n]

            s[i] = n
            n+=1