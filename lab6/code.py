from lab6 import RBTree

rtb = RBTree()
lst = ["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"]
for e in lst:
    rtb.insert(e)
    print(rtb)

rtb = RBTree()
lst = ["A", "C", "E", "H", "L", "M", "P", "R", "S", "X"]
for e in lst:
    rtb.insert(e)
    print(rtb)
