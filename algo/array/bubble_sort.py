# author: ptj
#
# 问题：冒泡排序。
# 时间复杂度：O(n^2), 空间复杂度O(1)

def bubble_sort(nums: list) -> list:
    last_swap = len(nums) - 1
    while last_swap > 0:
        sorted = True
        for j in range(last_swap):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                sorted, last_swap = False, j
        if sorted:
            break
    return nums
