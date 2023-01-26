from Node import Node

class Tree:
    """
    Tree class to represent n-tree 
    
    Attributes
    ----------
    None
    
    Methods
    -------
    Level_Order_traversal(self):
        Prints the level order traversal algorithm

    insert(self, values: list):
        Creates the node and its corresponging children

    insert_child(self, parent: Node, child: int):
        Creates the child nodes and the corresponding relation with their parent

    Level_Order_Search(self, value: int):
        Searches and returns the object Node if it is present in the tree.
    """
    def __init__(self, values:list = None):
        """
        Constructs the tree with the specified data, if children is not 
        None then insert function is called
        Attributes
        ----------
        values: list. information of a node and its children
        """
        self.root = None
        if values is not None:
            self.insert(values)
    
    def Level_Order_traversal(self):
        """
        Prints the level order traversal algorithm

        Attributes
        ----------
        None.
        """
        P = self.root
        traversed = []
        traversed.append(P)
        if P is None:
            return None
        while traversed != []:
            print(traversed[0].data)
            x = traversed.pop(0) 
            if x.children:
                traversed.extend(x.children)

    def insert(self, values: list):
        """
        Creates the node and its corresponging children. It checks
        if the node exists, if it does then it appends the children
        to that node, if it doesn't and error raises.

        Attributes
        ----------
        values: list. information of a node and its children
            values[0] is the information of the node
            values[1] is the information of the children of the node
        """
        if self.root is None:
            self.root = P = Node(values[0])
            if values[1] is not None:
                for child in values[1]:
                    self.insert_child(P, child)
        else:
            P = self.Level_Order_Search(values[0])
            if(P is not None):
                if values[1] is not None:
                    for child in values[1]:
                        self.insert_child(P, child)
            else:
                print("Debe digitar un valor que exista")
        return self.root
    
    def insert_child(self, parent: Node, child: int):
        """
        Creates the child nodes and the corresponding relation with their parent

        Attributes
        ----------
        parent: Node. Node object with the information of the parent of the children
        child: int. value to create the node.
        """
        Child_node = Node(child)
        parent.children.append(Child_node)
    
    def Level_Order_Search(self, value: int):
        """
        Searches and returns the object Node if it is present in the tree.

        Attributes
        ----------
        value: int. value to be searched in the tree.
        """
        traversed = []
        traversed.append(self.root)
        if self.root is None:
            return None
        while traversed != []:
            if traversed[0].data == value:
                return traversed[0]
            x = traversed.pop(0) 
            if x.children:
                traversed.extend(x.children)
        return None
