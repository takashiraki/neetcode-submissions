class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            # 数字はここで止まる
            if c not in ["+", "-", "*", "/"]:
                stack.append(int(c))
                continue
            
            b = stack.pop()
            a = stack.pop()
            print(a,b)
            k = 0
            if c == "+":
                k = a + b
            elif c == "-":
                k = a - b
            elif c == "/":
                k = int(a / b)
            elif c == "*":
                k = a * b
            stack.append(int(k))

        return stack[0]