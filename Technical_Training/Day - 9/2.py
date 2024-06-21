class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None

    def add_element(self,curr,x):
        if curr is None:
            return node(x)
        else:
            if x>=curr.data:
                curr.right=self.add_element(curr.right,x)
            else:
                curr.left=self.add_element(curr.left,x)
        return curr
a=tree()
a.add_element(a.root,10)
a.display(a.root)