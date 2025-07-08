class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercaseString=s.lower()
        # for i in lowercaseString:
        #     if (lowercaseString==lowercaseString[::-1]):
        #         return True
        #     else:
        #         return False    

        # Remove non-alphanumeric characters and convert to lowercase
        st1 = ''.join(c.lower() for c in s if c.isalnum())
        # Check if cleaned string is equal to its reverse
        return st1 == st1[::-1]


        