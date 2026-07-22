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

        print(new)

        check = True

        for i in range(len(new)):
            if new[i] != new[len(new)-1-i]:
                check = False

        return check
        