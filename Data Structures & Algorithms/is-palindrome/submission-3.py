class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(c.lower() for c in s if c.isalnum())
        
        left: int = 0
        right: int = len(string) - 1

        while left < right:
            if (string[left] != string[right]):
                return False
            left += 1
            right -= 1

        return True