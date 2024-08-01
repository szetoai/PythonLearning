class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp, length = '', 0
        final = ''
        for x in range(len(str1)):
            
            if 