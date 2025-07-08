class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1=s.split() #it store the splited string in list
        for i in list1:
            return len(list1[-1])
        