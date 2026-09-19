class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.n = nums
        

    def add(self, val: int) -> int:
        
        self.n.append(val)
        self.n.sort()
        return self.n[-self.k]
