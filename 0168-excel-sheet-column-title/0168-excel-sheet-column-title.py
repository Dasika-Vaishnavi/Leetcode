class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(65 + columnNumber%26))
            columnNumber //= 26
        return ''.join(reversed(result))


# only for 2 letter and 1 letter combo
# temp = []
# iter = ""
# alpha = [chr(i) for i in range(65, 91)]
# for i in range (0, len(alpha)):
#     for j in range(0, len(alpha)):
#         iter = alpha[i] + alpha[j]
#         temp.append(iter)
# temp = alpha + temp
# return (temp[columnNumber-1])
