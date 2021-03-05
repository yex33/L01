class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        if self.left is None:
            return
        node = self.left
        self.left = node.right
        if node.right is not None:
            node.right.parent = self
        node.right = self
        if self.parent is not None:
            if self.is_left_child():
                self.parent.left = node
            else:
                self.parent.right = node
            node.parent = self.parent
        else:  # self is root
            node.parent = None
        self.parent = node

    def rotate_left(self):
        if self.right is None:
            return
        node = self.right
        self.right = node.left
        if node.left is not None:
            node.left.parent = self
        node.left = self
        if self.parent is not None:
            if self.is_left_child():
                self.parent.left = node
            else:
                self.parent.right = node
            node.parent = self.parent
        else:
            node.parent = None
        self.parent = node


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        # You may alter code in this method if you wish, it's merely a guide.
        # Case 1: node is the root
        if node.parent is None:
            node.make_black()
        # Case 2: two red children
        elif node.get_brother() is not None and node.get_brother().is_red():
            node.make_black()
            node.get_brother().make_black()
            node.parent.make_red()
            # recursively fix the red color parent
            self.fix(node.parent)
        elif node.is_right_child():
            # Case 3: left-right red
            if node.parent.is_red():
                node.parent.rotate_left()
                # transformed into Case 5
                self.fix(node.left)
            # Case 4: right-leaning red
            else:
                node.parent.rotate_left()
                # before rotation node is the left child of root
                if node.parent is None:
                    self.root = node
                node.make_black()
                node.left.make_red()
        # Case 5: left-left red
        elif node.parent.parent is not None and node.parent.is_red():
            node.parent.parent.rotate_right()
            node.parent.make_black()
            node.get_brother().make_red()
            # before rotation node is the left-left grandson of root
            if node.parent.parent is None:
                self.root = node.parent
            # transformed into Case 2
            self.fix(node)

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
