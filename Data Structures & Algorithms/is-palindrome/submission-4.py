class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:

            while (s[start].isalnum() == False) and (start < end):
                start += 1
            while (s[end].isalnum() == False) and (start < end):
                end -= 1
            
            print(s[start])
            print(end)
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True