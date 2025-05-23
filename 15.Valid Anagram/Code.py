class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # a = {}
        # for ch in s:
        #     a[ch] = a.get(ch, 0) + 1
        
        # for ch in t:
        #     if ch not in a:
        #         return False
        #     a[ch] -= 1
        #     if a[ch] == 0:
        #         del a[ch]

        # return not a
        
        count = [0] * 26 

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in count)
    

# Input: s = "anagram", t = "nagaram"
# Output: true