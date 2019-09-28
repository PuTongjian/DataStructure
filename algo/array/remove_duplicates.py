# author: ptj
#
# 问题：删除排序数组中的重复项。要求空间复杂度为O(1)
#
# 解决思路：使用两个速度不相同的指针，遍历一次数组，将所有重复项放到数组后端。
#
# 时间复杂度：O(n), 空间复杂度O(1)


def remove_duplicates(nums: list) -> int:
    if len(nums) <= 1:
        return len(nums)

    i = 0
    for num in nums:
        if nums[i] != num:
            i += 1
            nums[i] = num

    return i+1
