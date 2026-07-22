class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        longer = word1
        shorter = word2
        if len(word2) > len(word1):
            longer = word2
            shorter = word1
        
        print(longer)
        print(shorter)

        new = ""
        
        for i in range(len(longer)):
            if i > len(shorter) - 1:
                new += longer[i]
            else:
                new += word1[i]
                new += word2[i]

        return new

