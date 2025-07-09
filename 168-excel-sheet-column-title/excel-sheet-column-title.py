class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # shift for 1-based index
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result
 