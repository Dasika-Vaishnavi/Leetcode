class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd lenght
            #Binary search
            l, r = i, i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l + 1
                l -= 1
                r += 1

            #even length
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

        #Brute Force: intuitive approach O(n^3)
        #l = []
        # temp = []
        # for i in range(0, len(s)):
        #     for j in range(i, len(s)):
        #         l.append(s[i:j+1])
        # for i in l:
        #     if i == i[::-1]:
        #         temp.append(i)
        # return (max(temp, key=len))



        