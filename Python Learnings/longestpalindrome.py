# Given a string s, return the longest palindromic substring in s.

# A string is called a palindrome string if the reverse of that string is the same 
# as the original string.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def palindrome(s):
    if s == s[::-1]: return s
    
    start, size = 0, 1
    for i in range(1, len(s)):
        l, r = i - size, i + 1
        s1, s2 = s[l-1:r], s[l:r]
        
        if l - 1 >= 0 and s1 == s1[::-1]:
            start, size = l - 1, size + 2
        elif s2 == s2[::-1]:
            start, size = l, size + 1
            
    return s[start:start+size]

print(palindrome("cbbd"))