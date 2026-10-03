def is_pangram(sentence: str) -> bool:
    """
    Return True if the sentence contains every letter of the English alphabet.
    """
    
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False

    return True
