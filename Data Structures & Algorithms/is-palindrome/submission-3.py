class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''
        b = ''

        for n in s:
            print(n)

            if not n.isalnum():
                continue
            
            f = f + n.lower()
            b = n.lower() + b
        print(f,b)

        if f == b:
            return True
        return False