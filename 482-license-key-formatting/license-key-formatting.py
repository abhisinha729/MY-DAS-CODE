class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for ch in s:
            if ch == '-':
                continue
            chars.append(ch.upper())

        result = []
        count = 0
        for ch in reversed(chars): #reverse chars
            if count == k:
                result.append('-')
                count = 0
            result.append(ch)
            count += 1
        return ''.join(reversed(result))