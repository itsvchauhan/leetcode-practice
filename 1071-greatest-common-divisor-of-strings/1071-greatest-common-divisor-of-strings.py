class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        div = ""
        temp = ""

        longer = str2
        shorter = str1
        if len(str1) > len(str2):
            longer = str1
            shorter = str2
        
        for i in range(len(longer)):
            if longer[i] == shorter[i % len(shorter)]:
                div += longer[i]
            else:
                return ""
            
            check1 = False
            check2 = False

            for i in range(int(len(longer) / len(div) +1)):
                if div * i == longer:
                    check1 = True
                    
                if div * i == shorter and len(div * i) <= len(shorter):
                    check2 = True

                if check1 and check2:
                    temp = div
                    break
        
        return temp
    

        