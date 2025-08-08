class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_case=""
        for char in s:
            ascii_value=ord(char)
            if 65<=ascii_value<=90:   #A-Z in ascii
                lower_case+=chr(ascii_value +32)
            else:
                lower_case+=char
        return lower_case            