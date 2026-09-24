class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1 = Counter(arr1)
        in_arr2 = set(arr2)
        res = []

        for num in arr2:
            c = count1[num]
            while c > 0:
                res.append(num)
                c -= 1

        addLast = []
        for num in arr1:
            if num not in in_arr2:
                addLast.append(num)

        addLast.sort()
        return res + addLast