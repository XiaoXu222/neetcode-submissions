class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
        # encode = ""
        # for i in range(len(strs)):
        #     length = len(strs[i])
        #     encode += f"{length}" + "#" + strs[i]
        #     # else:
        #     #     encode += f"{length}" + "#" + "0"
        # return encode

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j
        return res

        # decode = []
        # i = 0
        # while i < len(s):
        #     length_str = ""
        #     while s[i]!= "#":
        #         length_str += s[i]
        #         i += 1
        #     length = int(length_str)
        #     if length:
        #         string = s[(i+1):(i+length+1)]
        #         decode.append(string)
        #         i += length + 1
        #     else:
        #         decode.append("")
        #         i += 1
        # return decode


