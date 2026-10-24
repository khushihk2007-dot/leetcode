class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for ch in s:
            if 'A' <= ch <= 'Z':
                ch = chr(ord(ch)+32)
            result += ch
        return result

