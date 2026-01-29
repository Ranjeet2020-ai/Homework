class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        """
        Remove the last element from the list and return its value
        
        Returns: The value of the removed element or None if list is empty
        """
        # If list is empty, return None
        if self._size == 0:
            return None
        
        # Get the value to return
        value = self._tail.data
        
        # If there's only one element in the list
        if self._size == 1:
            del self._head
            self._head = self._tail = None
        else:
            # Find the second-to-last node
            current = self._head
            while current.next != self._tail:
                current = current.next
            
            # Remove the last node
            del self._tail
            self._tail = current
            self._tail.next = None
        
        # Update list's size
        self._size -= 1
        
        return value