class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)

        
        need = Counter(s1)
        window = Counter(s2[:length])

        if window == need:
            return True
        
        left = 0

        for right in range(length, len(s2)):
            window[s2[right]] +=1
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            if window == need:
                return True

            left += 1

        return False
            