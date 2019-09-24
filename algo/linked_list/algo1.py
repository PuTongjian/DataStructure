# author: ptj

# 问题：寻找链表中的倒数第n个结点
#
# 解决思路：建立p_node和p_temp两个指针，并令他们都指向头链表头部。等p_temp移动了n次以后，
# 再开始移动p_node。接下来，同时移动这两个指针，直到p_tmep越过链表末尾为止。此时p_node所
# 指向的结点正是链表的倒数第n个结点。
#
# 时间复杂度O(n)，空间复杂度O(1)

# 定义单链表结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head: ListNode, n: int) -> ListNode:
    p_node = head
    p_temp = head
    move_count = 0

    while p_temp:
        p_temp = p_temp.next
        p_node = p_node.next if move_count >= n else p_node
        move_count += 1

    return p_node
