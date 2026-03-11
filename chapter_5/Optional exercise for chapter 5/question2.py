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

    def delete_node(self, data):
        """
        Delete the node containing the specified data from the BST.
        
        Parameters:
        - 'data': The data value to delete
        
        Returns: None
        """
        # Find the node to delete
        node_to_delete = self._find(data)
        
        # If node not found, nothing to delete
        if node_to_delete is None:
            return
        
        # Case 1: Node has no children (leaf node)
        if node_to_delete._left_child is None and node_to_delete._right_child is None:
            parent = node_to_delete._parent
            
            # If node is root
            if parent is None:
                self._root_node = None
            else:
                # Remove reference from parent
                if parent._left_child == node_to_delete:
                    parent._left_child = None
                else:
                    parent._right_child = None
            
            # Clean up the node
            node_to_delete._parent = None
            
        # Case 2: Node has only one child
        elif node_to_delete._left_child is None:  # Has only right child
            child = node_to_delete._right_child
            parent = node_to_delete._parent
            
            # If node is root
            if parent is None:
                self._root_node = child
                child._parent = None
            else:
                # Connect child to parent
                child._parent = parent
                if parent._left_child == node_to_delete:
                    parent._left_child = child
                else:
                    parent._right_child = child
            
            # Clean up the node
            node_to_delete._left_child = None
            node_to_delete._right_child = None
            node_to_delete._parent = None
            
        elif node_to_delete._right_child is None:  # Has only left child
            child = node_to_delete._left_child
            parent = node_to_delete._parent
            
            # If node is root
            if parent is None:
                self._root_node = child
                child._parent = None
            else:
                # Connect child to parent
                child._parent = parent
                if parent._left_child == node_to_delete:
                    parent._left_child = child
                else:
                    parent._right_child = child
            
            # Clean up the node
            node_to_delete._left_child = None
            node_to_delete._right_child = None
            node_to_delete._parent = None
            
        # Case 3: Node has two children
        else:
            # Find the in-order successor (smallest node in right subtree)
            successor = node_to_delete._right_child
            while successor._left_child:
                successor = successor._left_child
            
            # Copy successor's data to the node to delete
            node_to_delete.data = successor.data
            
            # Now delete the successor (which will have at most one child)
            # This is recursive but we handle it inline
            
            # Successor's parent
            succ_parent = successor._parent
            
            # Successor's right child (successor has no left child by definition)
            succ_child = successor._right_child
            
            # If successor is the direct right child of node_to_delete
            if succ_parent == node_to_delete:
                # Connect node_to_delete's right to successor's right child
                node_to_delete._right_child = succ_child
                if succ_child:
                    succ_child._parent = node_to_delete
            else:
                # Successor is deeper in the tree
                # Connect successor's parent's left to successor's right child
                succ_parent._left_child = succ_child
                if succ_child:
                    succ_child._parent = succ_parent
            
            # Clean up the successor node
            successor._left_child = None
            successor._right_child = None
            successor._parent = None