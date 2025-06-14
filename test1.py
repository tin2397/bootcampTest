def list_to_int(lst: list) -> int:
    """
    Convert a list of integers to a single integer.
    
    Args:
        list (list): A list of integers.
        
    Returns:
        int: The integer formed by concatenating the elements of the list.
    """
    my_int = 0
    for i in lst:
        # Ensure the element is an integer before using it
        if not isinstance(i, int):
            raise ValueError(f"{i} is not an integer.")
        my_int = my_int * 10 + i
    return my_int

if __name__ == "__main__":
    # Example usage
    example_list_wrong = [1, 2, 3, "a"]
    example_list = [8,3,5,1]
    result = list_to_int(example_list)
    print(f"The integer formed from the list {example_list} is: {result}")
