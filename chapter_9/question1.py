def insertion_sort(array):
    # Start from the second element (index 1) 
    # as the first element is already "sorted" by itself
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        # Move elements of array[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            
        # Place the key in its correct position
        array[j + 1] = key

# --- Test Case from the image ---
array = [6, 8, 5, 1, 2]
insertion_sort(array)
