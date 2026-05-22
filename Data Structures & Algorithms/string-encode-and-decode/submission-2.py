import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        # 各単語の先頭に文字数#をくっつける
        wl = ""
        for s in strs:
            l = len(s)
            lw = [str(l).zfill(4) ,"#", s]
            w = "".join(lw)
            wl = wl + w
        print (wl)
        return wl

    def decode(self, s: str) -> List[str]:
        wl = []
        # 数字と#の位置を取得
        ll = [
            {"value" : m.group(1), "pos" : m.end(1)}
            for m in re.finditer(r'(\d{1,3})#', s)
        ]
        
        for l in ll:
            val = l["value"]
            pos = l["pos"]
            print(val, pos)
            k = ""
            i = 1
            for ll in range(int(val)):
                k = k + s[int(pos) + i]
                i += 1
            wl.append(k)
        return wl