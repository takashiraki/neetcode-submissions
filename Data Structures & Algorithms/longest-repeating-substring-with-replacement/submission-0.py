class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxCount = 0
        res = 0

        for r in range(len(s)):
            # 右側ポインタの出現回数
            count[s[r]] = count.get(s[r], 0) + 1

            # 出現回数とそれまでの出現回数最大値を比較
            maxCount = max(maxCount, count[s[r]])

            # ウィンドウサイズと連続数が無効の間はポインタを進める
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            
            # 左のポインタを進めた後に、ウィンドウサイズと過去最大数を比較して更新
            res = max(res, r - l + 1)
        
        return res