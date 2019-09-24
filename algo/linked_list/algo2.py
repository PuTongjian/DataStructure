# author: ptj

# 问题：判断链表中是否包含环？找出环的入口结点。
#
# 解决思路：问题1——弗洛伊德循环查找算法。用两个速度不相同的指针来遍历链表。只要二者相遇，就说明链表中有循环。
#           问题2——在解决问题1的基础上，令其中一个指针指向链表的头结点，并且令两个指针都继续移动，只不过每次
#           只走一个结点而已。两者再度相遇之处，就是循环的入口结点。（图伦方面的知识）
#
# 时间复杂度O(n)，空间复杂度O(1)

# 定义单链表结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head: ListNode) -> bool or ListNode:
    if not head or not head.next:
        return False

    p_fast = head
    p_slow = head

    while p_fast and p_fast.next:
        p_slow = p_slow.next
        p_fast = p_fast.next.next
        if p_fast is p_slow:
            # 存在环,则寻找环入口
            p_fast = head
            while p_fast is not p_slow:
                p_slow = p_slow.next
                p_fast = p_fast.next

            return p_slow

    return False
