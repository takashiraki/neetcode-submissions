class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for i in strs:
            ss = "".join(sorted(i))

            if ss in s:
                # 存在する場合
                s[ss].append(i)
            else:
                s[ss] = [i]
            
        return list(s.values())