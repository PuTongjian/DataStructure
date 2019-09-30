# author: ptj
#
# 问题：选择排序。
# 时间复杂度：O(n^2), 空间复杂度O(1)

def select_sort(nums: list) -> list:
    """
    选择排序，时间复杂度O(n^2)，空间复杂度O(1)
    """
    for i in range(len(nums)):
        pos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[pos]:
                pos = j
        nums[i], nums[pos] = nums[pos], nums[i]
    return nums
