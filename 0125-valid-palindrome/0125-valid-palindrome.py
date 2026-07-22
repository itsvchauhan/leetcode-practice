class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if c.isalpha() == False and c.isnumeric() == False:
                new += ""
            else:
                if c.isupper() == True:
                    c = c.lower()
                new += c

        for i in range(int(len(new)/2)):
            if new[i] != new[len(new)-1-i]:
                return False         
        else:
            return True
        