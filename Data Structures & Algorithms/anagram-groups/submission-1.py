from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()

        for x in strs:
            key = "".join(sorted((x)))
            if key in store:
                store[key].append(x)
            else:
                store[key] = [x]
        return list(store.values())
        