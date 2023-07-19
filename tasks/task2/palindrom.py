def isPalindrome(s: str) -> bool:
    s = s.lower()

    s = ''.join(char for char in s if char.isalnum())

    return s == s[::-1]