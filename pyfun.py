def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Formats a string with optional prefix, suffix, capitalization, and max length.

    Parameters:
    - text (str): Required. The main string to format.
    - prefix (str): Optional. Add before text. Default is "".
    - suffix (str): Optional. Add after text. Default is "".
    - capitalize (bool): Optional. Capitalize first letter. Default is False.
    - max_length (int): Optional. Max length of result. Default is None (no limit).

    Returns:
    - str: The formatted string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length is not None and (not isinstance(max_length, int) or max_length < 0):
        raise ValueError("max_length must be a non-negative integer or None")

    if capitalize:
        text = text.capitalize()

    result = f"{prefix}{text}{suffix}"

    if max_length is not None:
        result = result[:max_length]

    return result

# Example usage
print(format_text("hello", prefix="*", suffix="*", capitalize=True, max_length=10))  # *Hello*
