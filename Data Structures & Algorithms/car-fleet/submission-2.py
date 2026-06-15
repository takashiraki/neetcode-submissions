class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            
            # 残りの距離
            r = target - p
            print("rest:", r)
            
            # 到着時間
            t = r / s
            print("time:", t)
            stack.append([p, s, r, t])
        stack = sorted(stack, key=lambda x:x[0],reverse=True)
        print("stack:",stack)
        stack_2 = []
        mt = 0
        o = 0
        for l in stack:
            print("l",l)
            if l[3] > mt:
                o += 1
                mt = l[3]

            stack_2.append(l[3])
        print("stack 2", stack_2)
        print("mt", mt)
        print("o",o)

        return o
