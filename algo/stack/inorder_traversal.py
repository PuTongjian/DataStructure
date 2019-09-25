# author: ptj

# 问题：二叉树的中序遍历。
#
# 时间复杂度O(n)，空间复杂度O(n)

# 定义二叉树结点.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorder_traversal(root: TreeNode) -> list:
    stack, output = [], []
    cur_node = root

    while cur_node or stack:
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left

        node = stack.pop()
        output.append(node.val)
        cur_node = node.right

    return output
