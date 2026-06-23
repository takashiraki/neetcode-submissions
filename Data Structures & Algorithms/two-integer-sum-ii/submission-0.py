class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        for n in numbers:
            t = target - n
            ct = numbers.copy()
            ct.pop(i)

            if t in ct:
                return [i + 1, numbers.index(t) + 1]

            i += 1