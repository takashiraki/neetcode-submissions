class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. ポインタ作る
        # 2. t hash
        # 3. 冒頭三文字ハッシュ化
        # 4. 右のポインタ調整


        need = Counter(t)
        have = 0
        need_count = len(need)
        window = Counter()

        res = ""
        res_len = float("inf")
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if window[c] == need[c]:
                have += 1

            while have == need_count:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = s[left:right + 1]
                
                window[s[left]] -= 1
                if window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res
            