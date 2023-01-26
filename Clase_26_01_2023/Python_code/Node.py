class Node:
    """
    Node class to represent data
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    """
    def __init__(self, data: str, children:list = None):
        """
        Constructs the Node with the specified data
        Attributes
        ----------
        data: str. information of the  node. e.g. Unique name
        children: list. list of node to whom this node is parent.
        """
        self.children = []
        self.data = data

    #def __str__(self):
    #    return "value: "+self.data+" Children: "+ \
    #        ' -> '.join([str(child) for child in self.children])
    
    def __str__(self):
        children = ' -> '.join([str(child) for child in self.children])
        return "value: "+ self.data + " Children: "+\
            children