def check_balance(text):
    """
    Check if brackets in the text are balanced.
    """
    stack = []  # Using Python list as stack
    bracket_pairs = {
        ')': '(',
        ']': '[', 
        '}': '{'
    }
    opening_brackets = set(['(', '[', '{'])
    
    for i, char in enumerate(text):
        if char in opening_brackets:
            # Push opening bracket with its position
            stack.append((char, i))
        elif char in bracket_pairs:  # char is a closing bracket
            if not stack:
                return f"Match error at position {i}"
            
            top_char, _ = stack.pop()
            if top_char != bracket_pairs[char]:
                return f"Match error at position {i}"
    
    if stack:
        # There are unmatched opening brackets
        _, pos = stack[0]  # Get position of first unmatched
        return f"Match error at position {pos}"
    
    # Count bracket pairs
    bracket_count = sum(1 for char in text if char in opening_brackets)
    return f"Ok - {bracket_count}"