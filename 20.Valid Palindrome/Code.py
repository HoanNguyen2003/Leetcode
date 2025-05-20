class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# .isalnum() checks if the character is alphanumeric (a-z, A-Z, 0-9)
# .lower() converts the character to lowercase

# Input: s = "A man, a plan, a canal: Panama"
# Output: true