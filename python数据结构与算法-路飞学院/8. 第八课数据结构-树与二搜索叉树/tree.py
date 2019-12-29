class Node:
    # 节点对象
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type # "dir" or "file"
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


# n = Node("hello")
# n2 = Node("world")
# n.children.append(n2)
# n2.parent = n
# print(n2.parent.name)

class FileSystemTree:
    def __init__(self):
        self.root = Node("/") # 根目录的名字为空
        self.now = self.root

    def mkdir(self, name):
        # name 以斜杠结尾
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self, name):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'

        if name == "../":
            self.now = self.now.parent
            return

        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        else:
            raise ValueError("invalid dir")



tree = FileSystemTree()
tree.mkdir("var")
tree.mkdir("bin")
tree.mkdir("usr")
tree.cd('bin')
tree.mkdir('python')
tree.cd("../")
tree.ls("")
print(tree.ls(""))



