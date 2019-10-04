# author: ptj
#
# 问题：堆排序。
# 时间复杂度：O(nlogn), 空间复杂度O(1)

def heapify(array: list, size: int, parent: int):
    left = parent * 2 + 1
    right = parent * 2 + 2
    index = parent
    if left < size and array[left] > array[index]:
        index = left
    if right < size and array[right] > array[index]:
        index = right
    if index != parent:
        array[index], array[parent] = array[parent], array[index]
        heapify(array, size, index)


def heap_sort(array: list):
    size = len(array)
    index = (size - 2) // 2  # 最后一个小堆的父节点索引

    # 构造大顶堆
    for i in range(index, -1, -1):
        heapify(array, size, i)

    # 堆排序
    for i in range(size-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
