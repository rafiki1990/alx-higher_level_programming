def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
    text: text to be printed
    """
    if text is None:
        raise TypeError("text_indentation() missing 1 required"
                        "positional argument: 'text'")

    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string.")

    special_chars = ['.', '?', ':']
    lines = []
    current_line = ''
    for char in text:
        current_line += char
        if char in special_chars:
            lines.append(current_line.strip())
            current_line = ''

    lines.append(current_line.strip())
    if lines[-1] == '':
        lines.pop()  # Remove the last blank line if it's empty
    print('\n\n'.join(lines))
