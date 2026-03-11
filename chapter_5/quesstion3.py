class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'

class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        # Check if node has two children
        if node._left_child is not None and node._right_child is not None:
            raise ValueError("Cannot detach a node with two children")
        
        # Determine the child of the node to detach (if any)
        child = None
        if node._left_child is not None:
            child = node._left_child
        elif node._right_child is not None:
            child = node._right_child
        
        # Get the parent of the node
        parent = node._parent
        
        # Case 1: Node is the root node
        if parent is None:
            # The root node is being detached
            if child is not None:
                # Root has one child, make that child the new root
                self._root_node = child
                child._parent = None
            else:
                # Root has no children, tree becomes empty
                self._root_node = None
        else:
            # Case 2: Node is not the root
            if child is not None:
                # Node has one child
                # Connect the child to the parent
                child._parent = parent
                
                # Determine if node was left or right child of its parent
                if parent._left_child == node:
                    parent._left_child = child
                else:
                    parent._right_child = child
            else:
                # Node has no children (leaf node)
                # Simply remove the reference from the parent
                if parent._left_child == node:
                    parent._left_child = None
                else:
                    parent._right_child = None
        
        # Detach the node completely (optional but good practice)
        node._parent = None
        node._left_child = None
        node._right_child = None