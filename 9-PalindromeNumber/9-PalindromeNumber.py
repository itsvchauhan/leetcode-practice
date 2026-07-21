# Last updated: 7/20/2026, 10:29:53 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        l = len(temp)
        print(l)
        check = True

        for i in range(l):
            if temp[i] != temp[l-i-1]:
                return False
        else:
            return True