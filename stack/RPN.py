class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opera = ['+', '-', '*', '/']
        stack = []
        
        for token in tokens:
            if token not in opera:
                stack.append(token)
            else:
                opera_1 = stack.pop()
                opera_2 = stack.pop()
                res = eval(str(opera_2) + token + str(opera_1))
                stack.append(int(res))
                
        return stack.pop()
