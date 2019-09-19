# 定义 单链表 结构
# 数据存储类型为 int
#
# author: ptj


class Node:
    """
      定义单链表的结点
    """

    def __init__(self, data: int, next_node: object = None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, data: int):
        self._data = data

    @property
    def next_node(self) -> object:
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: object):
        self._next_node = next_node


class LinkedList:
    """
      定义单链表结构
    """

    def __init__(self):
        self._head = None
        self._tail = self._head
        self._size = 0

    def get_data_by_index(self, index: int) -> int:
        """
          根据索引获取结点的值
          时间复杂度为O(n)
        """
        node = self.__get_node_by_index(index=index)
        return node.data

    def get_node_by_index(self, index: int) -> Node:
        """
          根据索引获取结点对象
          时间复杂度为O(n)
        """
        return self.__get_node_by_index(index=index)

    def insert_after(self, data: int, index: int):
        """
          将新节点插入到改索引结点之后
          时间复杂度为O(n)
        """
        point = self.__get_node_by_index(index=index)
        node = Node(data=data, next_node=point.next_node)
        point.next_node = node

    def insert_before(self, data: int, index: int):
        """
          将新节点插入到改索引结点之前
          时间复杂度为O(n)
        """
        if index == 0:
            self.insert_to_head(data=data)
            return

        point = self.__get_node_by_index(index=index - 1)
        node = Node(data=data, next_node=point.next_node)
        point.next_node = node

    def insert_to_tail(self, data: int):
        """
          尾插入
          时间复杂度为O(1)
        """

        node = Node(data=data)

        if self._tail:
            self._tail.next_node = node
        else:
            self._head = node

        self._tail = node
        self._size += 1

    def insert_to_head(self, data: int):
        """
          头插入
          时间复杂度为O(1)
        """
        if self._head:
            self._head = Node(data=data, next_node=self._head)
        else:
            self._head = Node(data=data)
            self._tail = self._head

        self._size += 1

    def __get_node_by_index(self, index: int) -> Node:
        """
          根据索引获取结点对象
        """
        if index > self._size:
            raise Exception

        point = self._head
        i = 0
        while i < index:
            point = point.next_node
            i += 1

        return point





