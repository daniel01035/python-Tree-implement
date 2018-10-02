class Tree:

    def __init__(self, l):
        l.insert(0, 0)
        self.li = l


    def Preorder(self, current):
        if current < len(self.li) and self.li[current] is not None:
            print(self.li[current], end=' ')
            self.Preorder(2 * current)
            self.Preorder(2 * current + 1)

    def Inorder(self, current):
        if current < len(self.li) and self.li[current] is not None:
            self.Inorder(2 * current)
            print(self.li[current], end=' ')
            self.Inorder(2 * current + 1)

    def Postorder(self, current):
        if current < len(self.li) and self.li[current] is not None:
            self.Postorder(2 * current)
            self.Postorder(2 * current + 1)
            print(self.li[current], end=' ')