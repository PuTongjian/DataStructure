# 数据结构和算法
### 从原理到代码实现，一步步掌握常用的数据结构和算法。

---

## 数组（Array）
数组是一种**顺序存储结构**，当数组被声明时它会划分出一块连续的地址。正因为它是连续的，利用元素的索引（index）可以计算出该元素对应的存储地址。 

![数组.gif](https://images2018.cnblogs.com/blog/772743/201804/772743-20180410233420469-136207805.gif)  

**优点：**
- 无论数组有多大，根据索引位置只需要一次操作就可货取元素的内容，**查询效率高**。数组的**查询**操作的**时间复杂度为O(1)**。 

**缺点：**
- 同样因为数组的内存地址是连续的，插入（删除）一个元素时，该元素的所有后继元素都要挪动位置，所以**插入和删除操作效率低下**。数组的**插入和删除**操作**时间复杂度为O(n)**。
![插入.gif](https://images2018.cnblogs.com/blog/772743/201804/772743-20180410235302025-1349081730.gif)
- 大小固定，不支持扩展。

注意：当**有序线性表**查找的**时间复杂度为O(1)** 时，折中查找的**时间复杂度为O(logN)**。

---

## 链表(Linked list)
链表是一种**链式存储结构**，它是一种**线性表**，但是并不会按线性的顺序存储数据，而是在每一个节点里存到下一个节点的指针(Pointer)，将一些不连续的内存空间串连起来。  

**优点：**
- 链表在插入和删除操作时只需要改变某一结点的指针域，所以**插入和删除操作效率高**，**时间复杂度为O(1)**。
- 大小不固定，支持扩展。

**缺点：**
- **索引访问慢**，**时间复杂度为O(n)**

### [单向链表](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/data_structure/linked_list.py)
![链表.png](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png)  
链表中最简单的一种是**单向链表**，它包含两个域，一个信息域和一个指针域。这个链接指向列表中的下一个节点，而最后一个节点则指向一个空值。

### [双向链表]()
![双向链表.png](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)  
在单向链表的基础上，每个节点有两个两个指针，一个指向前驱节点，另一个指向后驱节点。

### [循环链表]()
![循环链表.png](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/350px-Circularly-linked-list.svg.png)  
普通链表的尾节点后继指针指向`None`，而循环链表的尾节点后继指针指向头节点

### 相关算法
- [寻找链表中的倒数第n个结点。](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/linked_list/algo1.py)  
**解决思路**：建立p_node和p_temp两个指针，并令他们都指向头链表头部。等p_temp移动了n次以后，再开始移动p_node。接下来，同时移动这两个指针，直到p_tmep越过链表末尾为止。此时p_node所指向的结点正是链表的倒数第n个结点。  
**算法复杂度**：时间复杂度O(n)，空间复杂度O(1)。

- [判断链表中是否包含环？找出环的入口结点。](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/linked_list/algo2.py)  
**解决思路**：问题1——弗洛伊德循环查找算法。用两个速度不相同的指针来遍历链表。只要二者相遇，就说明链表中有循环。问题2——在解决问题1的基础上，令其中一个指针指向链表的头结点，并且令两个指针都继续移动，只不过每次只走一个结点而已。两者再度相遇之处，就是循环的入口结点。（图伦方面的知识）  
**算法复杂度**：时间复杂度O(n)，空间复杂度O(1)。

- [反转单链表。](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/linked_list/algo3.py)  
**算法复杂度**：时间复杂度O(n)，空间复杂度O(1)。

---

## 栈（LIFO, Last In First Out）
堆栈（stack）又称为栈或堆叠，是一种抽象数据类型，只允许在有序的线性数据集合的一端（堆栈顶端, top）进行加入数据（push）和移除数据（pop）的运算。因而按照**后进先出**（LIFO, Last In First Out）的原理运作。  
![栈.jpg](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569309160255&di=624ef4d95ef9fc4236ba9ff26486de96&imgtype=0&src=http%3A%2F%2Fimg2018.cnblogs.com%2Fblog%2F1782005%2F201908%2F1782005-20190830125740215-836966875.jpg)

### 相关算法
- [逆波兰表达式求值](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/stack/RPN.py)
- [后序遍历二叉树](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/stack/postorder_traversal.py)
- [前序遍历二叉树](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/stack/preorder_traversal.py)
- [中序遍历二叉树](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/stack/inorder_traversal.py)

---

## 队列（queue）
队列，是**先进先出（FIFO, First-In-First-Out）的线性表**。在具体应用中通常用链表或者数组来实现。队列只允许在后端（rear）进行插入操作，在前端（front）进行删除操作。  
![队列.jpg](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569315841239&di=4e0260dad33873aeff13ac69dddcad0f&imgtype=0&src=http%3A%2F%2Ffile.koolearn.com%2F20141012%2F14130787585637.jpg)

### 相关算法
- [设计一个循环双端队列](https://github.com/PuTongjian/DataStructure-Algorithm/blob/master/algo/queue/circular_deque.py)

---

## 优先队列(priority queue)
优先队列不再遵循先入先出的原则,从”**优先**“一词，可看出有“**插队现象**”。优先队列至少含有两种操作的数据结构：**insert（插入）**，即将元素插入到优先队列中（入队）；以及**deleteMin（删除最小者）**，它的作用是找出、删除优先队列中的最小的元素（出队）。  
优先队列的实现常选用**二叉堆**，在数据结构中，**优先队列一般也是指堆**。  
**堆的两个性质：**
- 结构性：**堆是一个完全二叉树**。
- 堆序性：由于我们想很快找出最小元，则最小元应该在根上，**任意节点都小于它的后裔**，这就是**小顶堆（Min-Heap）**；如果是查找最大元，则最大元应该在根上，**任意节点都要大于它的后裔**，这就是**大顶堆(Max-heap)**。

---

## 哈希表（Hash table）
哈希表（也叫散列表），是根据键（Key）而直接访问在内存存储位置的数据结构。也就是说，它通过计算一个关于键值的函数，将所需查询的数据映射到表中一个位置来访问记录，这加快了查找速度。这个映射函数称做**哈希函数**，存放记录的数组称做**哈希表**。  
**基本概念：**
- 若关键字为 k，则其值的存放位置为F(k)。称这个对应关系**F**为**哈希函数**，按这个思想建立的**表**为**哈希表**。由此，查询只需通过一次运算，而无需遍历哈希表确定位置。查询的**时间复杂度为O(1)**。
- 对不同的关键字可能得到同一哈希地址，即k1 ≠ k2，而f(k1) = f(k2)，这种现象称为**冲突**。

---

## 二叉树和二叉搜索树

## 
