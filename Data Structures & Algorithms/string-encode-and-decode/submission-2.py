class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "/" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            slash = s.find("/", i)
            length = int(s[i:slash])
            res.append(s[slash + 1 : slash + 1 + length])
            i = slash + 1 + length
        return res