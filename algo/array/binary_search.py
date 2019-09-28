# author: ptj
#
# 问题：二分查找法。
# 时间复杂度：O(nlogn), 空间复杂度O(1)

def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1  # 查找范围 [l...r]

    while l<=r:
        mid = (l + r) // 2

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid

    return -1
