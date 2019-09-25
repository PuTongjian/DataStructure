# author: ptj

# 问题：二叉树的前序遍历。
#
# 解决思路：从根节点开始依次迭代，弹出栈顶元素输出到输出列表中，然后依次压入它的所有孩子节点，按照从上到下、从右到左的顺序依次压入栈中。
#
# 时间复杂度O(n)，空间复杂度O(n)

# 定义二叉树结点.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preorder_traversal(root: TreeNode) -> list:
  if not root:
      return []

  stack, output = [root], []

  while stack:
      node = stack.pop()
      output.append(node.val)

      if node.right:
          stack.append(node.right)
      if node.left:
          stack.append(node.left)

  return output
