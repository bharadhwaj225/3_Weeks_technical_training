class node:
    def _init_(self,u) :
        self.data=u
        self.prev=None
        self.nxt=None
class dll:
    def _init_(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.nxt=self.head
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def linear_search(self,target):
        t=self.head
        while t:
            if t.data==target:
                return t
            t=t.nxt
        return None

l1=dll()
l1.addback(29)
l1.addfront(13)
l1.addback(10)
l1.addback(55)
l1.addfront(33)
l1.display()
l1.rev_display()