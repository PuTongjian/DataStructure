# author: ptj

# 问题：逆波兰表达式求值。
#       示例 1：
#               输入: ["2", "1", "+", "3", "*"]
#               输出: 9
#               解释: ((2 + 1) * 3) = 9
#
# 时间复杂度O(n)，空间复杂度O(1)

def evalRPN(tokens: list) -> int:
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
