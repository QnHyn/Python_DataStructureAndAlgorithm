from bst import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0 # 节点的平衡因子默认为0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    # 情况一:不平衡是由于对K的右孩子的右子树插入导致的:左旋
    def rotate_left(self, p, c):
        # p和c分别对应图中的节点
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c
        # 更新balance factor(平衡因子)

        # 这个旋转函数只用在插入上没有任何问题。
        # 但是如果是删除导致的不平衡,bf要重新变换
        p.bf = 0
        c.bf = 0
        # 返回子树的根
        return c

    # 情况二:不平衡是由于对K的左孩子的左子树插入导致的:右旋
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        c.bf = 0
        p.bf = 0
        # 返回子树的根
        return c

    # 情况三:不平衡是由于对K的右孩子的左子树插入导致的:右旋-左旋
    def rotate_right_left(self, p, c):
        g = c.lchild
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c

        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf 左边重为1，右边重为-1
        if g.bf > 0: # 插入在S2上
            p.bf = 0
            c.bf = -1
        elif g.bf < 0: # 插入在S3上
            p.bf = 1
            c.bf = 0
        else: # S1 S2 S3 S4全是空 插入的是G本身
            p.bf = 0
            c.bf = 0
        # 返回子树的根
        return g

    # 情况四: 不平衡是由于对K的左孩子的右子树插入导致的:左旋 - 右旋
    def rotate_left_right(self, p, c):
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf 左边重为1，右边重为-1
        if g.bf < 0: # 插入在S3上
            p.bf = 0
            c.bf = 1
        elif g.bf > 0: # 插入在S2上
            p.bf = 0
            c.bf = -1
        else: # S1 S2 S3 S4全是空 插入的是G本身
            p.bf = 0
            c.bf = 0
        # 返回子树的根
        return g

    def insert_no_rec(self, val):
        # 1.BST二叉搜索树一样，先插入在调整
        p = self.root
        # 空树特殊处理
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild # node 存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild # node 存储的就是插入的节点
                    break
            else:
                return
        # 2. 更新我们的bf 从node的父亲开始,一直找到跟节点
        while node.parent: # node的parent不空
            if node.parent.lchild == node: # 传递是从左子树来的, 左子树更沉了
                # 更新node的parent的bf +1
                if node.parent.bf > 0:  # 原来的bf为1, 更新后变成2。 开始旋转
                    # 看node的哪边沉,决定旋转的方向
                    g = node.parent.parent # 为了练接旋转之后的子树
                    x = node.parent # 选转前node的parent
                    if node.bf < 0: # 左旋后右旋
                        n = self.rotate_left_right(node.parent, node)
                    else: # 右旋
                        n = self.rotate_right(node.parent, node)
                    # 记得把n和g连起来
                elif node.parent.bf < 0: # 原来的bf为-1, 更新后变成0
                    node.parent.bf = 0
                    break
                else: # 原来的bf为0, 更新后变成1
                    node.parent.bf = 1
                    # 继续循环
                    node = node.parent
                    continue
            else: # 传递是从右子树来的, 右子树更沉了
                # 更新node的parent的bf -1
                if node.parent.bf < 0:  # 原来的bf为-1, 更新后变成-2。 开始旋转
                    # 看node的哪边沉,决定旋转的方向
                    g = node.parent.parent  # 为了练接旋转之后的子树
                    x = node.parent  # 选转前node的parent
                    if node.bf > 0:  # 右旋后左旋
                        n = self.rotate_right_left(node.parent, node)
                    else: # 左旋
                        n = self.rotate_left(node.parent, node)
                    # 记得把n和g连起来
                elif node.parent.bf < 0:  # 原来的bf为1, 更新后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来的bf为0, 更新后变成-1
                    node.parent.bf = -1
                    # 继续循环
                    node = node.parent
                    continue
        # 连接选择后的子树
            n.parent = g
            if g: # g不为空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)


