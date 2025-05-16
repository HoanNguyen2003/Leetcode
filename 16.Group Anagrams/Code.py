class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = {} 
        print(anagrams)
        for word in strs:
            print(word)
            sorted_word = ''.join(sorted(word))  
            print(sorted_word)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
            print(anagrams)
        return list(anagrams.values())


# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]