# author: ptj
#
# 问题：选择排序。
# 时间复杂度：O(n^2), 空间复杂度O(1)

def insertion_sort(nums: list) -> list:
    """
        插入排序，时间复杂度O(n^2)，空间复杂度O(1)
    """
    for i in range(1, len(nums)):
        for j in range(i-1, 0-1, -1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

