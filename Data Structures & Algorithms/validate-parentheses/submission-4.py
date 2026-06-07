class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for c in s:
            if c in '({[':
                stack.append(c)
                continue
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False
            
        return not stack