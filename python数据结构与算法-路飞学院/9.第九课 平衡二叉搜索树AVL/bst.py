class BiTreeNode:
    # 二叉搜索树节点对象
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None  # 父节点


class BST:
    def __init__(self, li):
        self.root = None
        if li:
            for i in li:
                self.insert_no_rec(i)

    # 递归写法
    def insert(self, node, val):
        # 这里没有考虑等于的情况，可以统一归到左边或者右边。
        # 也可以给节点加个属性值。count计数它
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    # 非递归写法
    def insert_no_rec(self, val):
        p = self.root
        # 空树特殊处理
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    # 二叉搜索树的查询-递归写法
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node.data

    # 二叉搜索树的查询-非递归写法
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        # 情况1:node 是叶子节点
        if not node.parent:
            # 根节点
            self.root = None
        if node == node.parent.lchild:
            # 如果node是左孩子
            node.parent.lchild = None
            # node.parent = None
        else: # 右孩子
            node.parent.rchild = None
            # node.parent = None

    def __remove_node_21(self, node):
        # 情况2: node只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        # 它是它父亲的左孩子
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        # 它是它父亲的右孩子
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2: node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        # 它是它父亲的左孩子
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        # 它是它父亲的右孩子
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root: # 不是空树
            node = self.query_no_rec(val) # 这里query_no_rec返回的是一个对象
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild: # 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild: # 只有一个右孩子
                self.__remove_node_22(node)
            else: # 两个孩子都有
                # 找到右子树的最小值
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self, root):
        if self.root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    # 层次遍历
    def level_order(self, root):
        from collections import deque
        queue = deque()
        queue.append(root)
        while len(queue) > 0:  # 只要队列不为空,一直访问
            node = queue.popleft()
            print(node.data, end=",")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)


#tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
# 中序遍历实际上是对二叉搜索树的排序
#tree.in_order(tree.root)
#print(tree.query_no_rec(7).data)
#tree.delete(4)
#tree.in_order(tree.root)


