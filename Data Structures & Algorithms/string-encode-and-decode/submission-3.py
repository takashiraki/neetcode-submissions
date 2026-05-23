import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s):04d}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        wl = []
        i = 0
        while i < len(s):
            l = int(s[i:i+4])
            wl.append(s[i+4:i+4+l])
            i += l + 4
        return wl