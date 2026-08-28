class Solution:
    def minOperations(self, logs: List[str]) -> int:

        state = 0

        for op in logs:
            if op == "../":
                if state == 0:
                    continue
                else:
                    state -= 1
            elif op == "./":
                continue
            else:
                state += 1 
        
        return state
        