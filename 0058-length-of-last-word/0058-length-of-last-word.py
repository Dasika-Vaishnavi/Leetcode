class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = ""
        lst = []

        for i in s:
            if i != " ":
                temp += i
            else:
                if temp:
                    lst.append(temp)
                    temp = ""

        if temp:
            lst.append(temp)

        return len(lst[-1]) if lst else 0


