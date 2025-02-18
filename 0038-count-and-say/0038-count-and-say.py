class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"
        for _ in range(n - 1):
            seq = self.build_sequence(seq)
        return seq

    def build_sequence(self, s: str) -> str:
        result = []
        count = 1

        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(s[i])
                count = 1

        return "".join(result)