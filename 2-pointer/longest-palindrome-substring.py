class Solution(object):
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]

        substring = ''

        for i in range(len(s)):
            substring1 = expand(i,i)
            if len(substring1) > len(substring):
                substring = substring1
            substring2 = expand(i, i + 1)
            if len(substring2) > len(substring):
                substring = substring2
        return substring


    # Test case
    input_string = "babad"
    result = longestPalindrome(input_string)
    print(result)