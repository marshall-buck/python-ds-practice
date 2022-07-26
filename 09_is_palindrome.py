def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    new_string = phrase.replace(" ", "")
    original_phrase = list(new_string.lower())
    reverse_phrase = list(new_string.lower())

    reverse_phrase.reverse()

    return original_phrase == reverse_phrase
 
    #use notation from 05_reverse_string