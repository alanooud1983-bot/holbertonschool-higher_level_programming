#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Return tuple with length of string and its first character

    Args:
        sentence: The input string

    Returns:
        Tuple (length, first_character)
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
