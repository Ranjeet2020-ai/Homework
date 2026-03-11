def sift_down(array, start, end):
    """
    Sifts down the node at the 'start' index within the range up to 'end'.
    This implementation follows Max-Heap logic.
    """
    root = start
    
    while True:
        child = 2 * root + 1  # Left child index
        
        # If the left child is beyond the end of the range, we stop
        if child > end:
            break
            
        # If there is a right child and it is larger than the left child
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
            
        # If the parent is smaller than the largest child, swap them
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child  # Repeat for the swapped child's position
        else:
            # Parent is already in the correct place
            break

# --- Test Case from the image ---
array = [6, 2, 5, 8, 1]
sift_down(array, 1, 4)
