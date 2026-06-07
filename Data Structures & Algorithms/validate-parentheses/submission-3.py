class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in range(len(s)):
            if s[c] in '({[':
                stack.append(s[c])
                continue
            if stack == []:
                return False

            last = stack.pop()

            if last == "(" and s[c] != ")":
                return False

            if last == "[" and s[c] != "]":
                return False

            if last == "{" and s[c] != "}":
                return False
            
        return stack == []