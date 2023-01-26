from Tree import Tree

tree = Tree()

tree.insert(['raiz',['hijo_1','hijo_2','hijo_3']])
tree.insert(['hijo_2',['hijo_4','hijo_5']])
tree.insert(['hijo_1',['hijo_6']])
tree.insert(['hijo_3',None])
tree.insert(['hijo_6',['hijo_10']])


tree.Level_Order_traversal()