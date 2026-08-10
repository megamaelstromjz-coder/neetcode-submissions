import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        charSet = set(string.ascii_lowercase + string.digits)
        listS = list(s.lower())
        list1 = [x for x in listS if x in charSet]
        list2 = list(reversed(list1))

        if list1 == list2:
            return True
        else: 
            return False