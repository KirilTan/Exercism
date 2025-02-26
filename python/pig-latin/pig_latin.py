import re
from typing import List

# Define vowels as a set for faster membership checking
VOWELS = {'a', 'e', 'i', 'o', 'u'}


def translate(text: str) -> str:
    """
    Translates a sentence from English to Pig Latin.

    :param text: The input sentence in English.
    :return: The translated sentence in Pig Latin.
    """
    if not text.strip():
        return ""

    words = text.split()
    translated_words = [apply_pig_latin_rules(word) for word in words]
    return " ".join(translated_words)


def apply_pig_latin_rules(word: str) -> str:
    """
    Determines and applies the correct Pig Latin transformation based on word structure.

    :param word: The word to be translated.
    :return: The Pig Latin equivalent of the word.
    """
    if word.startswith(("xr", "yt")) or word[0] in VOWELS:
        return rule_one(word)

    if re.match(r"^[^aeiou]*qu", word):
        return rule_three(word)

    if re.match(r"^[^aeiou]+y", word):
        return rule_four(word)

    return rule_two(word)


def rule_one(word: str) -> str:
    """
    Rule 1: If a word starts with a vowel or 'xr'/'yt', add "ay" to the end.

    :param word: The word to be transformed.
    :return: Transformed word in Pig Latin.
    """
    return word + "ay"


def rule_two(word: str) -> str:
    """
    Rule 2: If a word begins with one or more consonants, move them to the end and add "ay".

    :param word: The word to be transformed.
    :return: Transformed word in Pig Latin.
    """
    first_vowel_index = next((i for i, char in enumerate(word) if char in VOWELS), len(word))
    return word[first_vowel_index:] + word[:first_vowel_index] + "ay"


def rule_three(word: str) -> str:
    """
    Rule 3: If a word starts with consonants followed by "qu",
    move the consonants and "qu" to the end, then add "ay".

    :param word: The word to be transformed.
    :return: Transformed word in Pig Latin.
    """
    qu_index = word.find("qu") + 2  # Move "qu" and any preceding consonants
    return word[qu_index:] + word[:qu_index] + "ay"


def rule_four(word: str) -> str:
    """
    Rule 4: If a word starts with one or more consonants followed by "y",
    move the consonants before "y" to the end, then add "ay".

    :param word: The word to be transformed.
    :return: Transformed word in Pig Latin.
    """
    y_index = word.find("y")
    return word[y_index:] + word[:y_index] + "ay"

