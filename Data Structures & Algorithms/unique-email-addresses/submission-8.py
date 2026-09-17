class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        op = set()
        
        for email in emails:

            at = email.index('@')

            domain = email[:at]
            local = email[at+1:]

            newDomain = ""

            for s in domain:
                if s == '.':
                    continue
                elif s =='+':
                    break
                else:
                    newDomain+=s
            
            em = newDomain + '@' + local
            
            op.add(em)
        
        print(op)
        return len(op)
