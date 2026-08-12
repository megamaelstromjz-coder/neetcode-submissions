class Solution:

    def subFunc (self, n, memory):
            
            if n == 0 or n == 1:
                return 1

            if memory[n] != -1:
                return memory[n]

            memory[n] = self.subFunc(n-1, memory) + self.subFunc(n-2, memory)
            
            return memory[n]

    def climbStairs(self, n: int) -> int:

        mem = [-1] * (n+1)

        return self.subFunc(n, mem)