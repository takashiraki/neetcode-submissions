class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        a = []

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        print(d)
        d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        print(d)

        i = 0
        for cd in d[:k]:
            a.append(cd[0])

        print(a)
        return a