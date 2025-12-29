def is_isogram(string: str) -> bool:
    letters = [ch.lower() for ch in string if ch.isalpha()]
    return len(letters) == len(set(letters))

print(is_isogram('Emily Jung Schwartzkopf'))
