class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        op = set()
        
        for email in emails:
            at = email.index('@')
            atDomain = email[at:]
            local = email[:at]
            localDots = [s for s in local if s != '.']
            
            plus = True if '+' in local else False

            if plus:
                pos = localDots.index('+')
                localDots = localDots[:pos]
                op.add(("".join(localDots)) + atDomain)

            else:
                op.add(("".join(localDots)) + atDomain)

        print(op)

        return len(op)
                

