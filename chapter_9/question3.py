def heap_sort(array):
    n = len(array)

    # Phase 1: Build a Max-Heap (Heapify)
    # Start from the last parent node and work backwards
    for start in range((n // 2) - 1, -1, -1):
        sift_down(array, start, n - 1)

    # Phase 2: Sort the array
    for end in range(n - 1, 0, -1):
        # Move current root (largest) to the end
        array[0], array[end] = array[end], array[0]
        # The heap size decreases, sift down the new root
        sift_down(array, 0, end - 1)