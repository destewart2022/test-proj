class BinTreeNode:
    def __init__(self,key,val):
        self.parent = None
        self.left   = None
        self.right  = None
        self.key = key
        self.val = val

    def __str__(self):
        s = 'BinTreeNode: Key: ' + str(self.key) + '; Value: ' + str(self.val) +  '; '
        if self.parent == None:
            s = s + 'Parent: None; '
        else:
            s = s + 'Parent: ' + str(self.parent.key) + '; '
        if self.left == None:
            s = s + 'Left: None; '
        else:
            s = s + 'Left: '+ str(self.left.key) + '; '
        if self.right == None:
            s = s + 'Right: None.'
        else:
            s = s + 'Right: ' + str(self.right.key) + '.'
        return s

    def findKey(self,key):
        if key == self.key:
            return self
        elif key < self.key:
            if self.left == None:
                return None
            else:
                return self.left.findNode(key)
        else:
            if self.right == None:
                return None
            else:
                return self.right.findNode(key)

    def insertKey(self,key,val):
        if self.key == key:
            self.val = val
            return self
        elif key < self.key: # insert in left sub-tree
            if self.left == None:
                n = BinTreeNode(key,val)
                self.left = n
                n.parent = self
                return n
            else:
                return self.left.insertKey(key,val)
        else:                # insert in right sub-tree
            if self.right == None:
                n = BinTreeNode(key,val)
                self.right = n
                n.parent = self
                return n
            else:
                return self.right.insertKey(key,val)

    def deleteNode(self):
        pass # Not implemented yet

    def inOrder(self):
        if self.left != None:
            for v in self.left.inOrder():
                yield v
        yield self
        if self.right != None:
            for v in self.right.inOrder():
                yield v

                

class BinTree:
    def __init__(self):
        self.root = None

    def findNode(self,key):
        if self.root == None:
            return None
        return self.root.findKey(key)

    def insertNode(self,key,val):
        if self.root == None:
            self.root = BinTreeNode(key,val)
        else:
            self.root.insertKey(key,val)

    def deleteNode(self,n):
        n.deleteNode()

    def __iter__(self):
        for v in self.root.inOrder():
            yield v

    def printInOrder(self):
        for v in self:
            print(v)


if __name__ == '__main__':
    import random
    names = ['Amy','Beth','Christine','Debbie','Ellen','Frances','Grace',
             'Hillary','Iris','Joan','Karen','Leah','Mary','Nellie','Olivia',
             'Petra','Queenie','Rhea','Samantha','Tracie','Uma','Victoria',
             'Wanda','Xena','Yvonne','Zoe']
    random.seed(2342544)
    names2 = random.sample(names,len(names))
    print(names2)
    bt = BinTree()
    for i in range(len(names2)):
        n = names2[i]
        bt.insertNode(n,i)
        print('Root:')
        bt.printInOrder()
        
