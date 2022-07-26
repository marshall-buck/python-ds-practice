def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    #iterate through string
    #if letter at index matches to_swap, swapcase()
    #return new string

    new_phrase = ""

    for char in phrase:
        if char == to_swap:
            new_phrase = new_phrase + char.swapcase()
        else:
            new_phrase = new_phrase + char
    
    return new_phrase