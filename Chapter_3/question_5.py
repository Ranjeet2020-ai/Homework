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
        raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        current = self._head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        current = self._head
        for _ in range(index):
            current = current.next
        current.data = value

    def append(self, value):
        new_node = ListNode(value, None, self._tail)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def pop(self):
        if self._size == 0:
            return None

        node = self._tail
        prev = node.prev

        if prev:
            prev.next = None
        else:
            self._head = None

        self._tail = prev
        value = node.data
        del node
        self._size -= 1

        if self._size == 0:
            self._head = self._tail = None

        return value

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise ValueError('Index out of bounds')

        if index == self._size:
            self.append(value)
            return

        current = self._head
        for _ in range(index):
            current = current.next

        prev = current.prev
        new_node = ListNode(value, current, prev)

        current.prev = new_node

        if prev:
            prev.next = new_node
        else:
            self._head = new_node

        self._size += 1

    def remove(self, index):
        # Check if index is out of bounds
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')

        current = self._head
        for _ in range(index):
            current = current.next

        prev = current.prev
        nxt = current.next

        value = current.data

        if prev:
            prev.next = nxt
        else:
            self._head = nxt

        if nxt:
            nxt.prev = prev
        else:
            self._tail = prev

        del current
        self._size -= 1

        if self._size == 0:
            self._head = self._tail = None

        return value

    def remove_by_value(self, value):
        current = self._head
        index = 0

        while current and current.data != value:
            current = current.next
            index += 1

        if not current:
            return None

        self.remove(index)
        return index

    def contains(self, value):
        for v in self:
            if v == value:
                return True
        return False

    def clear(self):
        current = self._head
        while current:
            nxt = current.next
            del current
            current = nxt

        self._head = self._tail = None
        self._size = 0