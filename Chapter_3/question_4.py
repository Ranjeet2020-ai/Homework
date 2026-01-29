class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
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
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node.data

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        current_node.data = value

    def append(self, value):
        new_node = ListNode(value, next=None, prev=self._tail)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def pop(self):
        if not self._size:
            return None

        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        if previous_node is None:
            self._head = None
        else:
            previous_node.next = None

        self._tail = previous_node

        value = node_to_remove.data
        del node_to_remove

        self._size -= 1

        if self._size == 0:
            self._head = self._tail = None

        return value

    def contains(self, value):
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        current_node = self._head
        while current_node:
            nxt = current_node.next
            del current_node
            current_node = nxt

        self._head = self._tail = None
        self._size = 0

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise ValueError('Index out of bounds')

        # Insert at end
        if index == self._size:
            self.append(value)
            return

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        previous_node = current_node.prev

        new_node = ListNode(value, next=current_node, prev=previous_node)

        current_node.prev = new_node

        if previous_node is None:
            self._head = new_node
        else:
            previous_node.next = new_node

        self._size += 1

