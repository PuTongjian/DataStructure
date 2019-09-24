# author: ptj

# 问题：反转单链表
#
# 时间复杂度O(n)，空间复杂度O(1)

# 定义单链表结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head: ListNode) -> ListNode:
    p_temp = None

    while head:
        p_next = head.next
        head.next = p_temp
        p_temp = head
        head = p_next

    return p_temp
