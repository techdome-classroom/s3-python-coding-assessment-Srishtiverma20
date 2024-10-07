def is_valid(s: str) -> bool:
    # Dictionary to hold matching pairs of parentheses
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'  # Get the top element or a dummy value if stack is empty
            if bracket_map[char] != top_element:  # Check if it matches the corresponding opening bracket
                return False
        else:  # If it's an opening bracket
            stack.append(char)  # Push it onto the stack

    # If the stack is empty, all brackets were matched correctly
    return not stack

