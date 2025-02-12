class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        for i in digits:
            temp += str(i)
        temp = str(int(temp)+1)
        fin = []
        for i in temp:
            fin.append(int(i))
        return fin
        