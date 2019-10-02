# author: ptj
#
# 问题：快速排序。
# 时间复杂度：O(nlogn), 空间复杂度O(logn)

def sort(nums: list) -> list:
    quick_sort(nums, 0, len(nums)-1)
    return nums


def partition(nums: list, left: int, right: int) -> int:
    pivot = nums[right]
    i = left-1

    for j in range(left, right):
        if pivot >= nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[right] = nums[right], nums[i+1]

    return i+1


def quick_sort(nums: list, left: int, right: int):
    if left < right:
        pivot = partition(nums, left, right)

        _quick_sort(nums, left, pivot-1)
        _quick_sort(nums, pivot+1, right)
