class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for s in strs:

            if s == "":
                output += "§"
            else:
                output += s + "±"
        
        return output 


    def decode(self, s: str) -> List[str]:

        op = []
        lastSplice1=0

        for i in range(len(s)):
            if s[i] == "±":
                op.append(s[lastSplice1:i])
                if i+1 < len(s):
                    lastSplice1 = i + 1
                else:
                    break
            if s[i] == "§":
                op.append("")
                if i+1 < len(s):
                    lastSplice1 += 1

        return op
