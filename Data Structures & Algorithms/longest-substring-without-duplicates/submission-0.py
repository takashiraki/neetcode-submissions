class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # 文字比較用
        l = 0 # 左のポインタ
        res = 0 # 結果

        for r in range(len(s)): # rが右のポインタ

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res